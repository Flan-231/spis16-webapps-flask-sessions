import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set in Heroku (Settings->Config Vars).  
                                     #To run locally, set in env.sh and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
   return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["Answer"]=request.form['Answer']
    if Answer == 'The overall temperature of the ocean increases':
        reply = "Your answer is correct!"
    elif Answer == 'The overall temperature of the coean decreases':
        reply = "Incorrect"  
    elif Answer == 'More ice blocks are formed.':
        reply = "Incorrect"
    else:
      reply=" Please make sure you've typed the answer in correctly"
   
      
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["response"]=request.form['response']
    if response == 'True':
        reply = "This is incorrect"
    elif response == 'False':
        reply = "Correct!" 
    else:
        reply=" Please make sure you've typed the answer in correctly"
   
        
    return render_template('page3.html')
    
if __name__=="__main__":
    app.run(debug=False)
