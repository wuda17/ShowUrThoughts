from crypt import crypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from blogsite.config import Config

#Initialize extensions at the begininng independent of a configuration object
db = SQLAlchemy()
bcrypt = Bcrypt()

login_manager = LoginManager()
#Passing in the login function name for the route that the extension should redirect to
login_manager.login_view = 'users.login'
#Class of the alert from bootstrap
login_manager.login_message_category = 'info'

#Automated email sending for reset token
mail = Mail()


#Creating a function for initializing the app, allows for multiple configurations for unit testing
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    #Import Blueprint objects and register to the app
    from blogsite.users.routes import users
    from blogsite.posts.routes import posts
    from blogsite.main.routes import main
    from blogsite.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
