
from flask import Flask, render_template,request
app = Flask(__name__)



@app.route("/")
def DojoForm():
    return render_template("index.html")

@app.route("/info", methods=["POST"])
def FormInfo():
    return render_template("info.html", name= request.form["name"], select1= request.form["select"],select2=request.form["select2"],comment=request.form["comment"])



if __name__=="__main__":
    app.run(debug=True)
