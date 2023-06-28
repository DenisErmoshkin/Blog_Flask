from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin
from app import login



@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):  # класс User - модель базы данных. Он наследуется от db.Model, и использует
    # ORM (объектно-реляционное отображение) для взаимодействия с базой данных.
    # автоматизирует перенос данных, хранящихся в таблицах реляционной базы данных
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):  #Метод __repr__ в Python является специальным методом, который используется для определения
        # строкового представления объекта. Когда вызывается функция repr() для объекта, она возвращает строку,
        # которая представляет объект таким образом, что эта строка может быть использована для создания эквивалентного
        # объекта с помощью функции eval() или при вводе в интерактивной оболочке.
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    # Столбец "id" - целочисленный тип данных, является первичным ключом
    id = db.Column(db.Integer, primary_key=True)
    # Столбец "body" - строковый тип данных, предназначен для хранения текста поста ограниченной длины (140 символов)
    body = db.Column(db.String(140))
    # Столбец "timestamp" - тип данных DateTime, предназначен для хранения даты и времени создания поста
    # Также установлен флаг index=True для индексирования этого столбца, что обеспечит более быстрый доступ к данным по времени
    # По умолчанию, используется текущая дата и время при создании записи
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # Столбец "user_id" - целочисленный тип данных, является внешним ключом, связанным с таблицей "user"
    # Это позволяет устанавливать связь между постом и пользователем, который его создал
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

