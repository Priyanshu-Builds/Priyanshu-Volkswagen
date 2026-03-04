from flask import Blueprint, render_template, request, redirect, url_for, make_response

auth_bp = Blueprint('auth', __name__, template_folder='../templates')

USERS = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'emp': {'password': 'emp123', 'role': 'employee'},
    'hr': {'password': 'hr123', 'role': 'hr'},
}


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        remember_me = request.form.get('remember_me')

        user = USERS.get(username)
        if user and user['password'] == password:
            role = user['role']

            if role == 'admin':
                redirect_url = url_for('admin.dashboard')
            elif role == 'employee':
                redirect_url = url_for('employee.dashboard')
            elif role == 'hr':
                redirect_url = url_for('hr.dashboard')
            else:
                redirect_url = url_for('auth.login')

            response = make_response(redirect(redirect_url))

            if remember_me:
                max_age = 60 * 60 * 24 * 7
                response.set_cookie('username', username, max_age=max_age)
                response.set_cookie('user_role', role, max_age=max_age)
            else:
                response.set_cookie('username', username)
                response.set_cookie('user_role', role)

            return response
        else:
            error = 'Invalid username or password. Please try again.'

    return render_template('auth/login.html', error=error)


@auth_bp.route('/logout')
def logout():
    response = make_response(redirect(url_for('auth.login')))
    response.delete_cookie('username')
    response.delete_cookie('user_role')
    return response
