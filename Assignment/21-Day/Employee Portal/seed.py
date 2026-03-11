from app import app
from models import db, User, Employee
from werkzeug.security import generate_password_hash

with app.app_context():
    if User.query.first():
        print("Database already has data. Skipping seed.")
    else:
        admin_user = User(
            username='admin',
            password=generate_password_hash('admin123'),
            role='admin'
        )
        manager_user = User(
            username='manager',
            password=generate_password_hash('manager123'),
            role='manager'
        )
        emp_user1 = User(
            username='employee',
            password=generate_password_hash('employee123'),
            role='employee'
        )
        emp_user2 = User(
            username='priyanshu',
            password=generate_password_hash('priyanshu123'),
            role='employee'
        )
        emp_user3 = User(
            username='ayush',
            password=generate_password_hash('ayush123'),
            role='employee'
        )
        db.session.add_all([admin_user, manager_user, emp_user1, emp_user2, emp_user3])
        db.session.flush()

        admin_emp = Employee(
            name='Admin User',
            email='admin@company.com',
            department='Administration',
            manager_id=None,
            user_id=admin_user.id
        )
        db.session.add(admin_emp)
        db.session.flush()

        manager_emp = Employee(
            name='Manager User',
            email='manager@company.com',
            department='Engineering',
            manager_id=admin_emp.id,
            user_id=manager_user.id
        )
        db.session.add(manager_emp)
        db.session.flush()

        emp1 = Employee(
            name='Employee User',
            email='employee@company.com',
            department='Engineering',
            manager_id=manager_emp.id,
            user_id=emp_user1.id
        )
        emp2 = Employee(
            name='priyanshu',
            email='priyanshu@company.com',
            department='Engineering',
            manager_id=manager_emp.id,
            user_id=emp_user2.id
        )
        emp3 = Employee(
            name='ayush',
            email='ayush@company.com',
            department='Marketing',
            manager_id=admin_emp.id,
            user_id=emp_user3.id
        )
        db.session.add_all([emp1, emp2, emp3])
        db.session.commit()
        print("Seed data inserted successfully!")
