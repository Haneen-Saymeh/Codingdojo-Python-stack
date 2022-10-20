
from flask import Flask
app = Flask(__name__)

@app.route("/")

def helloWorld():
    return "Hello World!"


@app.route("/dojo")

def dojo():
    return "Dojo!"


@app.route("/say/<var>")

def say(var):
    return f"Hi {var.capitalize()}"

@app.route("/repeat/<num>/<string>")
def repeatString(num, string):
    some_str = ""
    for i in range(int(num)):
        some_str += string
        some_str += " "
    return some_str

if __name__=="__main__":
    app.run(debug=True)

