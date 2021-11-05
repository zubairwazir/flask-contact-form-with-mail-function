from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/dbname'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(200))
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    org = db.Column(db.String(200))
    organization = db.Column(db.String(200))
    comments = db.Column(db.Text())

    def __init__(self, country, name, email, org, organization, comments):
        self.country = country
        self.name = name
        self.email = email
        self.org = org
        self.organization = organization
        self.comments = comments


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        country = request.form['country']
        name = request.form['name']
        email = request.form['email']
        org = request.form['org']
        organization = request.form['organization']
        comments = request.form['comments']
        
        if country == '' or name == '' or email == '' or org == '' or organization == '':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.email == email).count() == 0:
            data = Feedback(country, name, email, org, organization, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(country, name, email, org, organization, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted feedback')


if __name__ == '__main__':
    app.run(debug=True)
