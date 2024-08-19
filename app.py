from flask import Flask, render_template

# initialize the app
PORT = 3000
app = Flask(__name__)


@app.route('/')
def hello_flask():
    return render_template('index.html', context=)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
