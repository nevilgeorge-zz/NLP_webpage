from flask import Flask, render_template, url_for
import json, demjson
app = Flask(__name__)

# url_for("static", filename="style.css")
# url_for("static", filename="logic.js")

# json_data = open("results.json")
# data = json.load(json_data)
# print data

@app.route("/")
def index():
    # return "What?"
    name = {}
    return render_template('index.html')

@app.route("/winners")
def winners():
	json_data = open("output15.json")
	data = json.load(json_data)
	structured_data = data[u'structured']
	print structured_data
	return render_template('winners.html', data=structured_data)

@app.route("/jokes")
def jokes():
	json_data = open("funnytweets.json")
	data = json.load(json_data)
	return render_template('jokes.html', data=data)
	

if __name__ == "__main__":
    app.run()
