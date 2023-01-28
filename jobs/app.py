from flask import Flask, render_template

app = Flask(__name__)  # __name__ determines the root path of the app.


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
