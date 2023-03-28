from flask import Blueprint , render_template

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