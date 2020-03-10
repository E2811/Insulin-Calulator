from flask import Flask, flash, request, send_from_directory, render_template, json, redirect, url_for, session 
import sql_queries as S
import os
from werkzeug.utils import secure_filename
from predict import food_prediction
from USDA_api import get_CHO_food
from insulin import insulin_calculator

app = Flask(__name__, static_folder='./templates/')

@app.route('/')
def showmain():
    return render_template('index.html')

@app.route('/logIn',methods=['GET','POST'])
def logIn():
    ''' Log in as a user '''
    if request.method == "POST":
        data = request.form
        username = data["username"]
        password = data["password"]
        app.secret_key = 'esto-es-una-clave-muy-secreta'
        user_id = S.proveUser(username, password)[0]
        session['user_id'] = user_id
        if not user_id:
            return json.dumps({'html':'<span>Incorrect password</span>'})
        else:
            return redirect(url_for('upload_file'))
            #json.dumps({'user_id':user_id})
    return render_template('index.html')

@app.route('/signUp',methods=['GET','POST'])
def signUp():
    ''' Create new user '''
    if request.method == "POST":
        data = request.form
        username = data["username"]
        password = data["password"]
        weight = data['weight']
        if data.get('username', None) is not None and data.get('password', 
            None) and data.get('weight', None) is not None:
            S.adduser(username,password,weight)
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})
        
    return render_template('signup.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/fileUpload',methods=['GET','POST'])
def upload_file():
    ''' Upload a file '''
    UPLOAD_FOLDER = 'input/test'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            user_id = session['user_id']
            print(user_id)
            prediction = food_prediction(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            carbohydrates = get_CHO_food(prediction)['value']
            dose = insulin_calculator(carbohydrates, int(user_id))
            foto_id = S.addfoto(int(user_id),os.path.join(app.config['UPLOAD_FOLDER'], filename),prediction)[0]
            S.adddose(foto_id,carbohydrates, dose)
            return json.dumps({'dose':dose})
        #return redirect(url_for('uploaded_file',filename=filename))
    return render_template('fileupload.html')

if __name__ == "__main__":
    app.run(debug='True')