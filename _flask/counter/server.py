from tkinter import TRUE
from flask import Flask, render_template, request, redirect, session
app= Flask(__name__)
app.secret_key='secret'



    

@app.route("/")
def showcount():
    
    if 'hanin' in session:
        session['hanin'] += 1

    else:
        session['hanin']  =1 
    return render_template("index.html", counter=session['hanin'])


@app.route("/destroy")
def destroymain():
    session.clear()
    return redirect("/")

		

    




if __name__=="__main__":
    app.run(debug=True)

