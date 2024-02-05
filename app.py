from flask import Flask, render_template
import json

app = Flask(__name__)

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

@app.route('/')
def index():
    premium_data = load_data('premium.json')
    return render_template('index.html', premium_data=premium_data)

if __name__ == '__main__':
    app.run(debug=True)
