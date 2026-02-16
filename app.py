from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api')
def api():
    with open('data.json', 'r') as file:
        data = json.load(file)

    response = {
        "status": "success",
        "count": len(data),
        "data": data
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
