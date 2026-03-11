from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from models import db, User, Employee

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login first.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'role' not in session or session['role'] not in roles:
                flash('You do not have permission to access this page.', 'danger')
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('employees'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            employee = Employee.query.filter_by(user_id=user.id).first()
            if employee:
                session['employee_id'] = employee.id
            flash('Login successful!', 'success')
            if user.role == 'employee':
                return redirect(url_for('employee_profile', id=employee.id if employee else user.id))
            return redirect(url_for('employees'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


@app.route('/employees')
@login_required
@role_required('admin', 'manager')
def employees():
    all_employees = Employee.query.all()
    return render_template('employees.html', employees=all_employees)


@app.route('/employee/<int:id>')
@login_required
def employee_profile(id):
    employee = Employee.query.get_or_404(id)
    role = session.get('role')
    if role == 'employee':
        if session.get('employee_id') != id:
            flash('You can only view your own profile.', 'danger')
            abort(403)
    can_edit = False
    can_delete = False
    if role == 'admin':
        can_edit = True
        can_delete = True
    elif role == 'manager':
        manager_employee = Employee.query.filter_by(user_id=session['user_id']).first()
        if manager_employee and (employee.manager_id == manager_employee.id or employee.id == manager_employee.id):
            can_edit = True
    elif role == 'employee':
        if session.get('employee_id') == id:
            can_edit = True
    return render_template('employee_profile.html', employee=employee, can_edit=can_edit, can_delete=can_delete)


@app.route('/employee/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def employee_edit(id):
    employee = Employee.query.get_or_404(id)
    role = session.get('role')
    if role == 'admin':
        pass
    elif role == 'manager':
        manager_employee = Employee.query.filter_by(user_id=session['user_id']).first()
        if not manager_employee or (employee.manager_id != manager_employee.id and employee.id != manager_employee.id):
            flash('You can only edit your own team members.', 'danger')
            abort(403)
    elif role == 'employee':
        if session.get('employee_id') != id:
            flash('You can only edit your own profile.', 'danger')
            abort(403)
    else:
        abort(403)

    if request.method == 'POST':
        employee.name = request.form['name']
        employee.email = request.form['email']
        employee.department = request.form['department']
        if role == 'admin':
            new_role = request.form.get('role')
            if new_role and employee.user:
                employee.user.role = new_role
            new_manager_id = request.form.get('manager_id')
            if new_manager_id:
                employee.manager_id = int(new_manager_id) if new_manager_id != '' else None
            else:
                employee.manager_id = None
        db.session.commit()
        flash('Employee updated successfully!', 'success')
        return redirect(url_for('employee_profile', id=id))

    all_employees = Employee.query.filter(Employee.id != id).all() if role == 'admin' else []
    return render_template('employee_edit.html', employee=employee, all_employees=all_employees)


@app.route('/employee/<int:id>/delete', methods=['POST'])
@login_required
@role_required('admin')
def employee_delete(id):
    employee = Employee.query.get_or_404(id)
    if employee.user:
        db.session.delete(employee.user)
    db.session.delete(employee)
    db.session.commit()
    flash('Employee deleted successfully!', 'success')
    return redirect(url_for('employees'))


@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


if __name__ == '__main__':
    app.run(debug=True)
