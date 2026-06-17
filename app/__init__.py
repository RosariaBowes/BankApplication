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

from app.routes.root import *
from app.models.user import *
from app.models.user import insert_hyphens
app.jinja_env.filters['insert_hyphens'] = insert_hyphens

from .routes.root.user.receipt import *
from .routes.root.user.dashboard import *
from .routes.root.user.deposit import *
from .routes.root.user.transfer import *
from .routes.root.user.exchange import *
from .routes.root.user.recharge import *
from .routes.root.user.transaction_history import *
from .routes.root.user.receipt import *
from .routes.root.user.accounts import *
from .routes.root.user.accounts import *
from .routes.root.user.cards import *
from .routes.root.user.profile import *


