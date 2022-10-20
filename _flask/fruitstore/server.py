

from flask import Flask, render_template, request
app=Flask(__name__)


@app.route("/")
def storeapp():
    return render_template("index.html")


@app.route("/finalorder", methods=["post"])
def finalorder():
    sum = int(request.form["fruit1"])+int(request.form["fruit2"])+int(request.form["fruit3"])
    return render_template("appshow.html", fruit1=request.form["fruit1"],fruit2=request.form["fruit2"],fruit3=request.form["fruit3"], name=request.form["name"], id=request.form["id"], sum=sum)


if __name__=="__main__":
    app.run(debug=True)

