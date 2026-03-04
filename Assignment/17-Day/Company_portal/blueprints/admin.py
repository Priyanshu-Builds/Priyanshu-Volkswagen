from flask import Blueprint, render_template, request, redirect, url_for

admin_bp = Blueprint('admin', __name__, url_prefix='/admin', template_folder='../templates')


@admin_bp.route('/dashboard')
def dashboard():
    username = request.cookies.get('username')
    user_role = request.cookies.get('user_role')

    if not username or user_role != 'admin':
        return redirect(url_for('auth.login'))

    return render_template('admin/dashboard.html', username=username, role=user_role)
