from flask import Flask
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
import math


#for using local server 
local_server= True
with open('config.json', 'r') as c:
    params= json.load(c)["params"]

blogName= params["blog_name"]
app = Flask(__name__)
app.secret_key = 'super-secret-key'


if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    #in my project local server is same as production server
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]


db= SQLAlchemy(app)

class Posts(db.Model):
    # sno title content slug date
    sno = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), unique=False, nullable=False)
    sub_head = db.Column(db.String(180), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=False, nullable=False)
    slug = db.Column(db.String(25), unique=True, nullable=False)
    date = db.Column(db.String(50), unique=True, nullable=False)


class Contacts(db.Model):
    # sno name email phone_num message
    sno = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    phone_num = db.Column(db.String(10), unique=True, nullable=False)
    message = db.Column(db.String(50), unique=True, nullable=False)

@app.route('/')
def home():
    #     next: page+1
    # Last
    #     prev: page-1
    #     next: 0 
    post=Posts.query.filter_by().all()
    last= math.ceil(len(post)/int(params['no_of_params']))
    #[0:params['no_of_params']]
    
    page= request.args.get('page')

    
    
    if(not str(page).isnumeric()):
        page=1
    page=int(page)
    post=post[(page-1)*int(params['no_of_params']):(page-1)*int(params['no_of_params'])+int(params['no_of_params'])]
    if(page==1):
        prev= '#'
        next= '/?page='+ str(page+1)
    elif(page==last):
        prev= '/?page='+ str(page-1)
        next= '#'
    else:
        prev= '/?page='+ str(page-1)
        next= '/?page='+ str(page+1)

    return render_template('index.html', params=params, posts=post, prev=prev, next=next)

@app.route('/post/<string:post_slug>', methods=['GET'])
def post(post_slug):
    post=Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, posts=post)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    if('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.all()
        return render_template("dashboard.html", params=params, posts=posts)

    elif(request.method=='POST'):
        username= request.form.get('uname')
        userpass= request.form.get('password')
        if(username== params['admin_user'] and userpass== params['admin_password']):
            session['user']=username
            post=Posts.query.all()
            return render_template("dashboard.html", params=params, posts=post)
        elif(username!= params['admin_user'] or userpass!= params['admin_password']):
            return render_template("signin.html")
    else:
        return render_template('signin.html')


@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if('user' in session and session['user'] == params['admin_user']):
        if(request.method=='POST'):
            doc_title= request.form.get('title')
            doc_subhead= request.form.get('sub-head')
            doc_content= request.form.get('content')
            doc_slug= request.form.get('slug')
            date=datetime.now()

            if(sno=='0'):
                post= Posts(title=doc_title, sub_head=doc_subhead, content=doc_content, slug=doc_slug, date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title=doc_title
                post.sub_head=doc_subhead
                post.content= doc_content
                post.slug= doc_slug
                post.date= date
                db.session.commit()
                return redirect('/edit/'+sno)
    
    post = Posts.query.filter_by(sno=sno).first()
    return render_template('edit.html', params=params, post=post)


@app.route("/delete/<string:sno>", methods=['GET', 'POST'])
def delete(sno):
    if('user' in session and session['user'] == params['admin_user']):
        post= Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route('/about')
def about():
    return render_template('about.html')


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

    return render_template('contact.html', params=params)


