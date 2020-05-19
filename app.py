from Flask import Flask, render_template

app = Flask(_name_)


@app.route('/')
def home () :
    title = "Home Page"
    pageHeader = "This is the home page"
    return render_template("home.html", title=title, header=pageHeader)