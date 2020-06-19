from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/login')
def Hello():
    return render_template('login.html')
@app.route('/Login',methods=['post'])
def Login():
    user=request.form['UserName']
    if user=='sanjay':
        return render_template('Admin.html')
    else:
        return render_template('Guest.html')
if __name__=="__main__":
    app.debug=True
    app.run()