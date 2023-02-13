from flask import Flask, render_template, url_for, current_app, g, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello,Flaskbook!"


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
    return render_template(contact.html)


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # メールを送る

        # contactエンドポイントにリダイレクト
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")
