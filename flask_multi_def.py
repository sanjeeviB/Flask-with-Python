from flask import Flask
app = Flask(__name__)
@app.route('/')
def HellOWorld():
    return "<h1>HELLO WORLD!</h1>"
@app.route('/home')
def Home():
    return "<h2><i>welcome to Home Page!</i></h2>"
@app.route('/about')
def about():
    return "<h3><i>This is about Page!</i></h2>"

if __name__=='__main__':
    app.run(port=80)

