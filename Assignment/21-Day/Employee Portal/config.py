import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Priyanshu02@localhost:3306/employee_portal'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
