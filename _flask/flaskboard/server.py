from re import template
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<x>/<y>/<c1>/<c2>")
def board(x,y,c1,c2):
    return render_template("index.html", numx= int(x), numy=int(y), color_in1 = c1, color_in2=c2)


if(__name__)=="__main__":
    app.run(debug=True)