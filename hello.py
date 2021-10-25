from flask import Flask
app = Flask(__name__)

@app.route('/blog /<int:post ID>')
def hello(post ID):
    return 'blog number %d' %post ID

if __name__ == "__main__":
    app.run()