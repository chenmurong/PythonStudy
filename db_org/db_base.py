from peewee import *

db = MySQLDatabase('test', host='127.0.0.1', port=3306, user='root', passwd='123456', charset='utf8')
db.connect()


class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        charset = 'utf8'
        indexes = (
            ('password', False),
        )


if __name__ == '__main__':
    User.add_index(User.username)
    User.create_table()

