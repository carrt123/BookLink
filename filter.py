from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/hello/')
def hi():
    return 'hello'


app.run(debug=True)
