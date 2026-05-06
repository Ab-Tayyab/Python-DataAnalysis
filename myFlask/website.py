from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Home Page"

@app.route("/about")
def about():
    return "About"

@app.route("/contact")
def contact():
    return "<h2>Contact us</h2><p>Email: abdullahtayyab@gmail.com</p>"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)