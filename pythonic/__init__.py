import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_modals import Modal
from flask_mail import Mail
from pythonic.config import Config
from flask_admin import Admin

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate(db)
login_manager = LoginManager()
ckeditor = CKEditor()
modal = Modal()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()
admin = Admin()
app = Flask(__name__)
app.config[
    "SECRET_KEY"
] = "62913a7dac3933f87a84626fcdeaaf9e2653f0a000843efd9bf2b31ba4767402"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pythonic.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

from pythonic.adminbp.routes import MyAdminIndexView

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
ckeditor.init_app(app)
modal.init_app(app)
mail.init_app(app)
admin.init_app(app, index_view=MyAdminIndexView())

from pythonic.main.routes import main
from pythonic.users.routes import users
from pythonic.lessons.routes import lessons
from pythonic.courses.routes import courses_bp
from pythonic.errors.handlers import errors
from pythonic.adminbp.routes import adminbp

app.register_blueprint(adminbp)
app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(lessons)
app.register_blueprint(courses_bp)
app.register_blueprint(errors)

