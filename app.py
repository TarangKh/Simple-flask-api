from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

def fact(x) :
    res = 1
    for i in range(2, x+1) :
        res *= i
    return res

@app.route("/calculate_fact", methods = ["POST"])
def do_math() :
    if request.method == "POST" :
        num = int (request.form["number"])
        result_fact = fact(num)

        return render_template("results.html", result = result_fact)

if __name__=="__main__":
    app.run(host="0.0.0.0")
