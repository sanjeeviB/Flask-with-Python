from flask import Flask,render_template

app = Flask(__name__)

@app.route('/<name>')
def HellO(name):
    return render_template("hello.html",a=name)


if __name__=='__main__':
    app.debug=True
    app.run()
    #app.run(port=80)

