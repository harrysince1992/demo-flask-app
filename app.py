from flask import Flask, render_template
import os

# initialize the app
PORT = 3000
os.environ.setdefault('APP_COLOR', 'blue')
color = os.environ.get('APP_COLOR')
# color = 'blue'
app = Flask(__name__)


@app.route('/')
def hello_flask():
    return render_template('index.html', title='my application', bg_color=color)


@app.route('/info')
def get_info():
    return render_template('info.html', title='my application')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
