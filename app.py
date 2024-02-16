from flask import Flask, render_template,request
import getkey

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/result")
def logic():
    key=request.args.get("k")
    question=request.args.get("q")
    response=getkey.runPrompt(key,question)
    return "the result is {}".format(response)   
    


if __name__=='__main__':
    app.run(debug=True)

