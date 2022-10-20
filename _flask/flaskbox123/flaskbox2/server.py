from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play/<num>")
def boxtwo(num):
    return render_template("index.html", times=int(num))



if __name__=="__main__":
    app.run(debug=True)
