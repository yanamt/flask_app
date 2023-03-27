from flask import Blueprint,render_template

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