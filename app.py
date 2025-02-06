from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/home/<name>')
@app.route('/index/<name>')
def hello_arg(name):
    return f'<h1>Hello {escape(name)}!'




# if __name__ == '__main__':
#     app.run(debug=True)

