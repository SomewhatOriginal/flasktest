from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return("hey bro this is home / main")

@app.route("/<name>")
def user(name):
    return(f"hello {name}")

if __name__ == "__name__":
    app.run()