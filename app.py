from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import os
import json
# INIT THE APP
app = Flask(__name__)

# GET THE DB LOCATION
db_locatoin = 'sqlite:///database.sqlite'
# db_locatoin = f'sqlite:///{os.path.join(os.getcwd(), "database.sqlite" )}'

# CONFIGURE THE DATABASE URI
app.config['SQLALCHEMY_DATABASE_URI'] = db_locatoin
app.config['SECRET_KEY'] = 'MY SECRET KEY...'


# CONNECT THE DATABASE TO THE APP
db = SQLAlchemy(app)

# INITILISE THE DATABASE MODALS
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)

# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    posts = BlogPost.query.all()
    return render_template("index.html", posts=posts)

@app.route('/add-blog', methods=["GET", "POST"])
def add_blog():
    # CHEKC THE REQUEST METHOD
    if request.method == "POST":
        # CREATE A NEW BLOG POST
        title=request.form.get('title')
        subtitle=request.form.get('subtitle')
        body=request.form.get('body')
        new_post = BlogPost(
            title=title,
            subtitle=subtitle,
            body=body
        )

        # ADD THE POST TO DATABASE
        db.session.add(new_post)
        # SAVE THE POST IN DATABSE
        db.session.commit()
        # SHOW A FLASH MESSAGE
        flash('Post Added Successfully!', 'success')
        # REDIRECT TO HOME PAGE
        return redirect(url_for('home'))
    
    return render_template('create-post.html')

@app.route('/update-post/<int:post_id>', methods=["GET", "POST"])
def update_post(post_id):
    # GET THE POST FROM DATABASE
    blog_post = BlogPost.query.get(post_id)
    
    # CHECK IS THE POST THERE
    if not blog_post:
        # FLASH MESSAGE
        flash('Post Not Found!', 'error')
        # REDIRECT TO HOME PAGE
        return redirect(url_for('home'))
    
    # CHECK THE REQUEST METHOD
    if request.method == "POST":
        # GET DATA FROM FORM
        title=request.form.get("title")
        subtitle=request.form.get("subtitle")
        body=request.form.get('body')

        print(title, subtitle, body)


        # UPDATE THE POST
        blog_post.title = title
        blog_post.subtitle = subtitle
        blog_post.body = body
        # COMMIT THE CHANGES
        db.session.commit()
        # FLASH MESSAGE FOR UPDATE
        flash('Post Updated Successfully!', 'info')
        # REDIRECT USER TO HOME PAGE
        return redirect(url_for('home'))

    # REDIRECT TO THE POST PAGE AGAIN
    return render_template('create-post.html', post=blog_post)

@app.route('/post/<int:index>')
def get_post(index):
    # GET THE POST FROM DATABASE
    requested_post = BlogPost.query.get(index) 
    # RETURN IN TEMPLATE
    return render_template("post.html", post=requested_post)

@app.route('/delete-post/<int:post_id>')
def delete_post(post_id):
    # GET POST FROM DATABASE
    post_to_delete = BlogPost.query.get(post_id)
    # DELETE THE POST
    db.session.delete(post_to_delete)
    # SHOW A FLASH MESSAGE
    flash('Post Deleted Successfully!', 'error')
    # COMMINT CHANGES IN DATABASE
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
