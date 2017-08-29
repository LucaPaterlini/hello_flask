#!/usr/bin/python
from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello', methods=['POST', 'GET'])
def hello():
    return render_template('hello.html')

@app.route('/hello_world', methods=['POST', 'GET'])
def hello_world():
    print("Hello World!")
    return ""

if __name__ == '__main__':
    app.run(debug=False, threaded=True)