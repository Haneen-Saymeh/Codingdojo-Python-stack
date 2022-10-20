

from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def index():
    return "Helloooo"


@app.route("/hii")
def greet():
    return render_template("index.html")

@app.route("/<var>")
def greet2(var):
    arr1 = [1,2,3,4,5]
    myvars= [
        {"name":"hanz", "country":"china"}
    ]
    return render_template("index.html", name=var, var1 = arr1, var2 = myvars)

# when we want to use the array and list we usse the name of its variable var1 and var2 not arr1 and my vars







if(__name__)=="__main__":
    app.run(debug=True)