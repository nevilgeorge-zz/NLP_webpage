from flask import Flask, render_template, url_for
app = Flask(__name__)

# url_for("static", filename="style.css")
# url_for("static", filename="logic.js")

@app.route("/", )
def index():
    # return "What?"
    name = {}
    return render_template('index.html')

@app.route("/findwinners")
def find_winners():
	return render_template('table.html')

if __name__ == "__main__":
    app.run()