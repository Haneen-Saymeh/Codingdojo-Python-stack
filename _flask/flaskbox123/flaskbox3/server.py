from flask import Flask, render_template
app = Flask(__name__)


@app.route("/play/<num>/<color>")
def boxthree(num, color):
    return render_template("index.html", times=int(num), color_in= color)


if __name__=="__main__":
    app.run(debug=True)