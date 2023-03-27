from flask import Blueprint,render_template
from apps.app import db
from apps.crud.models import User

#Blueprintオブジェクト（crudアプリ）の作成
crud=Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

#indexエンドポイントを作成しindex.htmlを返す
@crud.route("/")
def index():
    return render_template("crud/index.html")

@crud.route("/sql")
def sql():
    db.session.query(User).all()
    return "コンソールログを確認してください"