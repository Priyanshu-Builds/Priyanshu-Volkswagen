from flask import Flask, redirect, url_for
from blueprints.auth import auth_bp
from blueprints.admin import admin_bp
from blueprints.employee import employee_bp
from blueprints.hr import hr_bp

app = Flask(__name__)
app.secret_key = 'company-portal-secret-key'

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(hr_bp)


@app.route('/')
def index():
    return redirect(url_for('auth.login'))


if __name__ == '__main__':
    app.run(debug=True)
