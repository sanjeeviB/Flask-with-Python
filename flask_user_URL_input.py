from flask import Flask
app = Flask(__name__)
@app.route('/user/<name>')
def HellOWorld(name):
    return "<h1>HELLO %s</h1>" %name
@app.route('/user1/<int:num>')
def HellO_num(num):
    return "<h1>HELLO %d</h1>" %num

@app.route('/home')
def Home():
    return "<h2><i>welcome to Home Page!</i></h2>"
@app.route('/about')
def about():
    return "<h3><i>This is about Page!</i></h2>"

if __name__=='__main__':
    app.debug=True
    app.run()
    #app.run(port=80)

 
