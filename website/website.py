from flask import Flask
import News

app = Flask(__name__)
app.register_blueprint(News.newsBluePrint, url_prefix='/news')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
