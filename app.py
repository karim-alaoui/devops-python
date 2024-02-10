from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/cities')
def cities():
    cities_list = ["London", "Paris", "Berlin", "Tokyo", "Sydney", "Toronto", "San Francisco", "Rome", "Shanghai"]
    return jsonify(cities_list)

@app.route('/countries')
def countries():
    countries_list = ["USA", "Canada", "UK", "Australia", "Germany"]
    return jsonify(countries_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
