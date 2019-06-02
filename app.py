from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return"welcome to pythonnnn"
@app.route('/home')
def home():
    return"myhome"
    
if(__name__=='__main__'):
    app.run(debug=True)