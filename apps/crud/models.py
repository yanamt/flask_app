from datetime import datetime

from apps.app import db
from werkzeug.security import generate_password_hash

#db.modelを継承したUserクラスを作成する
class User(db.Model):
    #テーブル名を指定
    __tablename__="users"
    #カラムを定義
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,index=True)
    email=db.Column(db.String,unique=True,index=True)
    password_hash=db.Column(db.String)
    created_at=db.Column(db.Datetime,default=datetime.now)
    updated_at=db.Column(db.Datetime,default=datetime.now,onupdate=datetime.now)

    #パスワードをリセットするためのプロパティ
    @property
    def password(self):
        raise 