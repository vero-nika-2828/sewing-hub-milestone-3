import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World...again!"


@app.route("/base.html")
def hello_base():
     return "Hello base this time!"



if __name__ == "__main__" :
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)
