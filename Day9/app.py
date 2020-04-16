from flask import Flask
from flask import render_template
app = Flask(__name__)
# @app.route("/soniya")
# def hello():
#     return "Hello Soniya! What are your hobbies?"
#
# @app.route("/naman")
# def nhello():
#     return "Hello Naman! Which is your fav. movie?"
#
# @app.route("/akanshu")
# def ahello():
#     return "Hello Akanshu! You are cool"

# @app.route("/<name>")
# def greetings(name):
#     return "Welcome " + name + "!"

# @app.route("/todo")
# def home():
#     return "<h1>Hello Friend</h1>"

@app.route("/html")
def func():
    return render_template("index.html")

@app.route("/page")
def funct():
    return render_template("page2.html")

if __name__ == "__main__":
    app.run(debug= True, host = "127.0.0.1", port=8080)
