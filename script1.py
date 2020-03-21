from flask import Flask, render_template

app = Flask(__name__)

echipe = [
    {'nume': 'Proiect 1', "marime": 10, 'bloc': "C10"},
    {'nume': 'Proiect Zero', "marime": 3, 'bloc': "E"},
    {'nume': 'Hero', "marime": 3, 'bloc': "21"},
]


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html", echipe=echipe, display=True)


if __name__ == "__main__":
    app.run(debug=True)
