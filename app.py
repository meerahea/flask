from flask import Flask , url_for

app = Flask(__name__)

@app.route("/")
def index():
    # Generate the URL for the 'about' endpoint
    about_url = url_for('about')
    return f"The URL for the about page is: {about_url}"

@app.route("/about")
def about():
    return "This is the about page."

if __name__=="__main__":
    app.run(host="0.0.0.0")
