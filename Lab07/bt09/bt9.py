from flask import render_template, Flask

app = Flask(__name__, static_folder='C:\\Users\\peo\\Documents\\GitHub\\Python\\Lab07\\bt9\\templates\\static')

@app.route('/')
def index():
    return render_template("bt9.html")

if __name__ == '__main__':
    app.run(port=5450)
