from flask import Flask, render_template, request, session
 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("project.html")

app.run(debug=True)