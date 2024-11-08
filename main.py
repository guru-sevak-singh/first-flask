from flask import Flask, render_template
from post import Post
import requests

posts = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()

post_object = []

for post in posts:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_object.append(post_obj)



app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", post=post_object)



print(post_object)
print(post_object[0].id)
print(post_object[0].title)



@app.route('/post/<int:index>')
def get_post(index):
    num_value = index-1
    requested_post = post_object[num_value]
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
