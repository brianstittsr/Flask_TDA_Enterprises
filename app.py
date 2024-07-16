from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/brianstitt/Documents/GitHub/FlaskProjects/TDAEnterprises/blog.db'

db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(100), nullable=False)
    posted_by = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text, nullable=False)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/about') 
def about():
    return render_template('about.html')

@app.route('/post') 
def post():
    return render_template('post.html')

@app.route('/contact') 
def contact():
    return render_template('contact.html')

@app.route('/add') 
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST']) 
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, posted_by="BrianStitt", content=content, date_posted=datetime.now())
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()