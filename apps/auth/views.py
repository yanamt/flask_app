from flask import Blueprint , render_template,flash,url_for,redirect,request
from apps.app import db
from apps.auth.forms import SignUpForm
from apps.crud.models import User
from flask_login import login_user


#Blueprintを使ってauthアプリを作成
auth=Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static"
)

#indexエンドポイントを作成
@auth.route("/")
def index():
    return render_template("auth/index.html")

@auth.route("/signup",method=["GET","POST"])
def signup():
    #Signupformのインスタンス化
    form=SignUpForm()
    if form.validate_on_submit():
        user=User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        if user.is_duplicate_email():
            flash("指定のメールアドレスは登録済みです")
            return redirect(url_for("auth.signup"))
        #ユーザー情報をデータベースに追加する
        db.session.add(user)
        db.session.commit()

        #ユーザー情報をsessionに登録する
        login_user(user)
        #GETパラメータにnextキーがあり，値が存在しない場合はユーザーの一覧ページへリダイレクトする
        print(request.args.get)
        next_=request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            next_=url_for("crud.users")
        return redirect(next_)
    return render_template("auth/signup.html",form=form)

        

