from flask import Flask, render_template, request, session
 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/main")
def firstPage():
    return render_template("home.html")

@app.route("/articles")
def history():
    return render_template("articles.html")

@app.route("/guide")
def guide():
    return render_template("guide.html")

@app.route("/articles/2023")
def guide1():
    return render_template("page23.html")

@app.route("/articles/2022")
def guide2():
    return render_template("page22.html")

@app.route("/articles/other")
def guide3():
    return render_template("pageother.html")

#сыллки и страницы для 2023 года

@app.route("/articles/2023/1")
def page231():
    return render_template("page231.html")

@app.route("/articles/2023/2")
def page232():
    return render_template("page232.html")

@app.route("/articles/2023/3")
def page233():
    return render_template("page233.html")


#сыллки и страницы для 2022 года

@app.route("/articles/2022/1")
def page221():
    return render_template("page221.html")

@app.route("/articles/2022/2")
def page222():
    return render_template("page222.html")

@app.route("/articles/2022/3")
def page223():
    return render_template("page223.html")

#сыллки и страницы для Другого...

@app.route("/articles/other/1")
def pageother1():
    return render_template("pageother1.html")

@app.route("/articles/other/2")
def pageother2():
    return render_template("pageother2.html")

@app.route("/articles/other/3")
def pageother3():
    return render_template("pageother3.html")

@app.route("/articles/other/4")
def pageother4():
    return render_template("pageother4.html")

@app.route("/articles/other/5")
def pageother5():
    return render_template("pageother5.html")

app.run(debug=True)