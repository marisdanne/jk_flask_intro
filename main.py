from flask import Flask, render_template, request, redirect
from file_proc import pievienot

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

@app.route('/postData', methods = ['POST', 'GET'])
def postData():
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        #print(request.form)
        vards = request.form.get('vards')
        pievienot(vards)
        return redirect('/kontakti')
    else:
        return "This method not supported!"

if __name__ == '__main__':
    app.run(port=80, debug=True)