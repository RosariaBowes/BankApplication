from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config.from_object(Config)

# load environment variables from the .env file
load_dotenv()

# Secret Key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# DB configurations
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app.models.user import insert_hyphens
app.jinja_env.filters['insert_hyphens'] = insert_hyphens

from app.routes.root import *
from app.models.user import *
from .routes.root.user.reciept import *