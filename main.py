from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/kontakti')
def kontakti():
    return render_template('kontakti.html')

@app.route('/parmani')
def parmani():
    return render_template('parmani.html')

@app.route('/jaunumi')
def jaunumi():
    return render_template('jaunumi.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=80, debug=True)