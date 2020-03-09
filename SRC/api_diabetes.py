from flask import Flask, request, render_template
import os


app = Flask(__name__, static_folder='./templates/css')

#@error_handler
@app.route("/user/create/<username>", methods=['GET'])
def create_user(username):
    return U.createUser(username) 

@app.route('/')
def showmain():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['GET'])
def signUp():
    # create user code will be here !!
    return 'hi'

if __name__ == "__main__":
    app.run(debug='True')