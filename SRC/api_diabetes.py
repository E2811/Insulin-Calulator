from flask import Flask, request, render_template
import sql_queries as S
import os


app = Flask(__name__, static_folder='./templates/')

@app.route('/')
def showmain():
    return render_template('index.html')

@app.route('/signUp',methods=['GET','POST'])
def signUp():
    ''' Create new user '''
    if request.method == "POST":
        data = request.form
        username = data['username']
        password = data['password']
        weight = data['weight']
        print(username)
        if data.get('username', None) is not None and data.get('password', 
            None) and data.get('weight', None) is not None:
            S.adduser(username,password,weight)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug='True')