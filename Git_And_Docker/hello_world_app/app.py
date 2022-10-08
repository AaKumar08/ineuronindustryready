from flask import Flask
app = Flask(__name__)

@app.route('/')
def health():
    return 'Health Check'

@app.route('/hello')
def hello_ji():
    return 'Hello World from Python Flask!'

app.run(host='0.0.0.0', port=6000)