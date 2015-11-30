from flask import Flask, render_template, url_for, request
import utils

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method=="GET":
		return render_template("index.html", answer="")
	else:
		query = request.form["query"]
		return render_template("index.html", answer=utils.answer(query))

@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == "__main__":
    	app.debug = True
	app.run(host='0.0.0.0',port=8000)
