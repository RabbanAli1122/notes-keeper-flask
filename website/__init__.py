from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager



db= SQLAlchemy()## SQLAlchemy instance created without app
DB_NAME = "database.db"# This sets the name of the database file that will be used. In this case, it is an SQLite database file called "database.db".


def create_app():
    app= Flask(__name__)
    app.config["SECRET_KEY"] = "sijjfkskadjfosdo fj"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}" #This line sets the database URI (connection string) for SQLAlchemy, which tells it what kind of database to connect to and how to connect to it.
    #app.config: This is a dictionary that stores configuration variables for your Flask app.
    #The "SQLALCHEMY_DATABASE_URI" key specifically holds the connection string for SQLAlchemy to know which database to use.
    #sqlite:///: This part tells SQLAlchemy to use SQLite as the database.
    #{DB_NAME}: This is a placeholder for the actual database file name.
    db.init_app(app)  #The purpose of db.init_app(app) is to connect the db object (which represents the database) to your Flask app. When you create the db object using SQLAlchemy(), it’s not linked to any specific app yet. By calling db.init_app(app), you are telling the db object to use the settings and context of your Flask app, such as where the database is located. This step is essential to make sure your app can interact with the database, perform queries, and manage data properly.
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User,Note # we do this because we want to define the USER and Note classes before creating database
    create_database(app)

    login_manager=LoginManager()
    login_manager.login_view="auth.login"#it tells what to do if user is not logined
    login_manager.init_app(app)

    @login_manager.user_loader #this decorator tells the flask use the following function to load a user
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app):
    if not path.exists("website"+DB_NAME):
        with app.app_context():
            db.create_all()#it creates database with all of the defined columns in models.py
        print("Created Database!")