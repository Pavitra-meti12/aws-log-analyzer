from flask import Flask, render_template, jsonify
import json
import os
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/report.json')
def report():

    time.sleep(1)

    file_path = os.path.join(
        os.getcwd(),
        'report.json'
    )

    with open(file_path, 'r') as file:
        data = json.load(file)

    return jsonify(data)

if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )