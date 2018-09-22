from flask import Flask,render_template, render_template, request 
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('world.html')

@app.route('/world/')
def world():
    name = request.args.get('name')
    mail = request.args.get('mail')
    return render_template('world.html', title='flask test', name=name, mail=mail) 

@app.route('/name/')
def name():
    name = request.args.get('name')
    return str(name) 

if __name__ == '__main__':
#    app.debug = True
    app.run(host='0.0.0.0')