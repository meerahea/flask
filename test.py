from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!!</h1>"

@app.route("/hello_world01")
def hello_world01():
    return "<h1>Hello, World01!!</h1>"

@app.route("/hello_world02")
def hello_world02():
    return "<h1>Hello, World02!!</h1>"

@app.route("/test")
def test():
    a = 5+6
    return "This is my function to run app {}".format(a)

@app.route("/test2")
def test2():
    data = request.args.get('x')
    return "This is a data input from my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
