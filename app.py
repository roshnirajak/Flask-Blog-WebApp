from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
# from flask_mail import Mail
# from waitress import serve 

#for using local server 
local_server= True
with open('config.json', 'r') as c:
    params= json.load(c)["params"]

blogName= params["blog_name"]
app = Flask(__name__)

# #mail
# app.config.update(
#     MAIL_SERVER ='smtp.gmail.com',
#     MAIL_PORT= "465",
#     MAIL_USE_SSL=True,
#     MAIL_USERNAME=params["gmail_uname"],
#     MAIL_PASSWORD=params["password"]
# )
# mail= Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    #in my project local server is same as production server
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]

db= SQLAlchemy(app)

class Contacts(db.Model):
    # sno name email phone_num message
    sno = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    phone_num = db.Column(db.String(10), unique=True, nullable=False)
    message = db.Column(db.String(50), unique=True, nullable=False)

@app.route('/')
def main():
    return render_template('index.html', params=params)

@app.route('/index')
def index():
    return render_template('index.html', params=params, )

@app.route('/about')
def about():
    return render_template('about.html', params=params)

@app.route('/post')
def post():
    return render_template('post.html', params=params)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    
    #catching data from html doc
    if request.method=='POST':
        doc_name= request.form.get('fname')
        doc_email= request.form.get('email')
        doc_phone_num= request.form.get('phone_num')
        doc_message= request.form.get('message')

        #storing data into variables from mysql
        entry= Contacts(name=doc_name, email=doc_email, phone_num=doc_phone_num, message=doc_message)
        db.session.add(entry)
        db.session.commit()
        # #sending message to email
        # mail.send_message('New message from Flask Blog from' + doc_name, 
        #                     sender=doc_email, 
        #                     recipients=[params["gmail_uname"]],
        #                     body=doc_message + "\m" + doc_phone_num,
        # )

    return render_template('contact.html', params=params)

if __name__ == '__main__':
    app.run(debug=True)
