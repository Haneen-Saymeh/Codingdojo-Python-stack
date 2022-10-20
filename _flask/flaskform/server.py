from urllib import request
from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def showform():
    return render_template("index.html")






@app.route("/process", methods=["POST"])
def form_process():
    return render_template("greet.html", name = request.form["username"], email= request.form["email"])


if __name__=="__main__":
    app.run(debug=True)