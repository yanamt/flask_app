from flask import Flask, render_template, url_for, current_app, g, request, redirect, flash,make_response,session
from email_validator import validate_email, EmailNotValidError
import logging
from flask_debugtoolbar import DebugToolbarExtension
import os
from flask_mail import Mail,Message

app = Flask(__name__)
# secret_keyの追加
app.config["SECRET_KEY"] = "2ajwjduxodfhpgj223er3red"
# ログレベルの設定
app.logger.setLevel(logging.WARNING)
# リダイレクト時に中断しないようにする
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
# DebugToolbarExtensionにアプリケーションをセットする
toolbar = DebugToolbarExtension(app)

# mailの設定を追加する
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

mail = Mail(app)


@app.route("/")
def index():
    return redirect(url_for("contact"))


@app.route("/hello/<name>", methods=["get"], endpoint="hello_endpoint")
def hello(name):
    return f"Hello,{name}!"


@app.route("/name/<name>")
def display_name(name):
    return render_template("index.html", name=name)


with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello_endpoint", name="yuta"))
    # /name/<name>
    print(url_for("display_name", name="yutaa"))
    # /static/style.css
    print(url_for("static", filename="style.css"))

# current_appにアクセス
ctx = app.app_context()
ctx.push()
print(current_app.name)
# g
g.connection = "connection"
print(g.connection)

with app.test_request_context("/users?updated=true"):
    print(request.args.get("updated"))


@app.route("/contact")
def contact():
    response=make_response(render_template("contact.html"))
    #クッキーの設定
    response.set_cookie("flaskbook key","flaskbook value")
    #セッションの設定
    session["username"]="ichiro"

    return response


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # メールを送る
        print(request)
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # 入力チェック
        is_valid = True
        if not username:
            flash("ユーザー名は必須です")
            is_valid = False
        if not email:
            flash("メールアドレスは必須です")
            is_valid = False
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False

        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False
        if not is_valid:
            return redirect(url_for("contact"))

        # メールを送る
        send_email(email,"お問合せありがとうございました","contact_mail",username=username,description=description)

        # contactエンドポイントにリダイレクト
        flash("問い合わせありがとうございました")
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")

def send_email(to,subject,template,**kwargs):
    #メールの送信を行うメソッド
    msg=Message(subject,recipients=[to])
    msg.body=render_template(template+".txt",**kwargs)
    msg.html=render_template(template+".html",**kwargs)
    mail.send(msg)

