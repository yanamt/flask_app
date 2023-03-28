from flask import Blueprint,render_template,redirect,url_for
from apps.app import db
from apps.crud.models import User
from apps.crud.forms import UserForm

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

#sqlエンドポイントの作成
@crud.route("/sql")
def sql():
    db.session.query(User).count()
    return "コンソールログを確認してください"

@crud.route("users/new",methods=["GET","POST"])
def create_user():
    #userformクラスをインスタンス化
    form=UserForm()
    #バリデートする
    if form.validate_on_submit():
        print(form.username)
        #ユーザーを作成し，データベース用のUserクラスを作成
        user=User(
        username=form.username.data,
        email=form.email.data,
        password=form.password.data,
        )

        #ユーザーを追加してコミットする
        db.session.add(user)
        db.session.commit()

        #ユーザーの一覧画面にリダイレクト
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html",form=form)

@crud.route("/users")
def users():
    #ユーザー一覧を取得する
    users=User.query.all()
    return render_template("crud/index.html",users=users)
@crud.route("/users/<user_id>",methods=["GET","POST"])
def edit_user(user_id):
    form=UserForm()
    
    #Userモデル(db)からユーザー情報を取得
    user=User.query.filter_by(id=user_id).first()

    if form.validate_on_submit():
        user.username=form.username.data
        user.email=form.email.data
        user.password=form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))
    return render_template("crud/edit.html",user=user,form=form)

@crud.route("/users/<user_id>/delete",methods=["POST"])
def delete_user(user_id):
    user=User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))
