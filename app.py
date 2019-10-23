from flask import Flask, render_template, request
from flask_cors import CORS
from models import *
import time

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(time.ctime(time.time()), name, post)

    posts = get_posts()

    who = who_login(request.remote_addr)

    return render_template('index.html', posts = posts, who = who)


if __name__ == "__main__":
	app.run(debug=True, host = "127.0.0.1", port="8080")
