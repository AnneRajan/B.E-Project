from flask import Flask, render_template,flash, url_for, request, session, redirect, jsonify
#from flask.ext.pymongo import PyMongo
from flask_pymongo import PyMongo
#from flask_mongoengine import MongoEngine
import bcrypt
import numpy as np


import tensorflow as tf
import keras
from keras.models import load_model



app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'jobprofile'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/jobprofile'




model = load_model('Job_Role_model.h5')
graph = tf.get_default_graph()

'''
import pickle
model = pickle.load(open('Job_Role_Pickle.sav', 'rb'))

'''


#mongo = MongoEngine(app)
mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template('index.html')
    
 
    
@app.route("/main")
def main():
    return render_template('main.html')

    
@app.route("/resume")
def resume():
    return render_template('resume.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
     
     if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'email' : request.form['email']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'first_name' : request.form['first_name'], 
                          'last_name' : request.form['last_name'], 
                          'company' : request.form['company'], 
                          'email' : request.form['email'], 
                          
                          'pass' : hashpass
                      })
            session['email'] = request.form['email']
            flash('Your account has been created! You are now able to log in', 'success')
       
            return redirect(url_for('signup'))
        
        return 'That email ID already exists!'

    
     return render_template('register.html')


@app.route("/login",methods=['GET','POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['email']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['email'] = request.form['email']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'


@app.route("/jobprofile")
def jobprofile():
    return render_template('jobprofile.html')

@app.route('/prediction',methods=['POST'])
def prediction():

    os          = request.form["os"]
    aoa         = request.form["aoa"]
    pc          = request.form["pc"]
    se          = request.form["se"]
    cn          = request.form["cn"]
    ma          = request.form["ma"]
    cs          = request.form["cs"]
    hac         = request.form["hac"]
    interest    = request.form["interest"]
    cert        = request.form["cert"]
    personality = request.form["personality"]
    mantech     = request.form["mantech"]
    leadership  = request.form["leadership"]
    team        = request.form["team"]
    selfab      = request.form["selfab"]

    myu = [77.00318789848731, 76.99831228903614, 77.07569696212026, 77.11301412676585, 76.9541817727216, 77.0150018752344, 77.060320040005, 5.002687835979497]
    sig = [10.071578660726848, 10.098653693844197, 10.137528173238477, 10.088164425588161, 10.018397202418788, 10.18533143324003, 10.095941558583263, 2.582645138598079]
    arr = [os,aoa,pc,se,cn,ma,cs,hac]

    for i in range(8):
        arr[i] = float(arr[i])
        arr[i] = (arr[i]- myu[i])/sig[i]

    inti     = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    certi    = [0,0,0,0,0,0,0]

    if interest == "analyst":
        inti[0] = 1
    elif interest == "hadoop":
        inti[1] = 1
    elif interest == "cloud":
        inti[2] = 1
    elif interest == "data":
        inti[3] = 1
    elif interest == "hacking":
        inti[4] = 1
    elif interest == "management":
        inti[5] = 1
    elif interest == "networks":
        inti[6] = 1
    elif interest == "programming":
        inti[7] = 1
    elif interest == "security":
        inti[8] = 1
    elif interest == "software":
        inti[9] = 1
    elif interest == "system":
        inti[10] = 1
    elif interest == "testing":
        inti[11] = 1
    elif interest == "web":
        inti[12] = 1

    if cert == "app":
        certi[0] = 1
    elif cert == "full":
        certi[1] = 1
    elif cert == "hadoop":
        certi[2] = 1
    elif cert == "security":
        certi[3] = 1
    elif cert == "machine":
        certi[4] = 1
    elif cert == "python":
        certi[5] = 1
    elif cert == "shell":
        certi[6] = 1

    for i in certi:
        arr.append(i)

    for i in inti:
        arr.append(i)

    if leadership == "yesl":
        arr.append(0)
        arr.append(1)
    else:
        arr.append(1)
        arr.append(0)

    if team == "yest":
        arr.append(0)
        arr.append(1)
    else:
        arr.append(1)
        arr.append(0)

    if personality == "extrovert":
        arr.append(1)
        arr.append(0)
    else:
        arr.append(0)
        arr.append(1)

    if selfab == "nos":
        arr.append(1)
        arr.append(0)
    else:
        arr.append(0)
        arr.append(1)

    if mantech == "man":
        arr.append(1)
        arr.append(0)
    else:
        arr.append(0)
        arr.append(1)


    print (arr)

    with graph.as_default():
        print("done in loop")
        y      = model.predict(np.array( [arr,]))
        result = np.where(y == np.amax(y))
        print(result[0])

    print("done1")



#Here i am printing this on the terminal but u have to put it like this on the website

    if result[1]==[0]:
        return render_template('jobprofile.html', prediction_text='Business Intelligence')
        print('Business Intelligence Analyst')
    elif result[1]==[1]:
        return render_template('jobprofile.html', prediction_text='Database Administrator')
        print('Database Administrator')
    elif result[1]==[2]:
        return render_template('jobprofile.html', prediction_text='Project Manager')
        print('Project Manager')
    elif result[1]==[3]:
        return render_template('jobprofile.html', prediction_text='Security Administrator')
        print('Security Administrator')
    elif result[1]==[4]:
        return render_template('jobprofile.html', prediction_text='Software Developer')
        print('Software Developer')
    else:
        return render_template('jobprofile.html', prediction_text='Technical Support')
        print('Technical Support')

    print("done2")

    
if __name__=='__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)