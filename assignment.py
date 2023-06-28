from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "“Welcome to ABC Corporation”"

@app.route("/")
def details():
    return "<h1>Company Name: ABC Corporation</h1><p>Location: India</p><p>Contact Details: 999-999-9999<p/>"



if __name__=="__main__":
    app.run(host="0.0.0.0")
