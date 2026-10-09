from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World from Vibha Gunturi! I am adding my first code change."

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')



if __name__ == "__main__":
    app.run(debug=True)