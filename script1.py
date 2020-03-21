from flask import Flask, render_template

app = Flask(__name__)


class Masina:
    def __init__(self, motor, roti, usi):
        self.motor = motor
        self.roti = roti
        self.usi = usi * 2


echipe = [
    {'nume': 'Proiect 1', "marime": 10, 'bloc': "C10"},
    {'nume': 'Proiect Zero', "marime": 3, 'bloc': "E"},
    {'nume': 'Hero', "marime": 3, 'bloc': "21"},
]


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/test/')
def test():
    return render_template("tw.html", garaj=[
        Masina("2L", '18', 3),
        Masina("1L", '14', 3.3),
        Masina("3", '5', 1.3),
    ])


@app.route('/about/')
def about():
    return render_template("about.html", echipe=echipe, display=True)


if __name__ == "__main__":
    app.run(debug=True)
