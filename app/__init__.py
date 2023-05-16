from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager #расширение управляет состоянием входа пользователя в систему, так что, например,
# пользователи могут войти в приложение, а затем перейти на разные страницы, пока приложение «помнит», что пользователь
# вошел в систему.

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes, models
