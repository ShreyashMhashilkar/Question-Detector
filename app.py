from flask import Flask,redirect,url_for,render_template,request
from detect_question import detectQuestion

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/",methods=["POST","GET"])
def get_ott():
    if request.method == "POST":
        question = request.form["question"]
        
        return redirect(url_for("display_result",quest = question))
    else:
        return render_template("index.html")

@app.route("/<quest>")
def display_result(quest):
    res = detectQuestion(quest)
    return render_template("result.html",result = res)

if __name__=="__main__":
    app.run(debug=True)