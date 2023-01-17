from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from waitress import serve 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
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
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method=='POST':
        doc_name= request.form.get('fname')
        doc_email= request.form.get('email')
        doc_phone_num= request.form.get('phone_num')
        doc_message= request.form.get('message')

        entry= Contacts(name=doc_name, email=doc_email, phone_num=doc_phone_num, message=doc_message)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
