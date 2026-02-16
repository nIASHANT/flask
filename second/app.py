from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas Connection
MONGO_URI = "mongodb+srv://<db_username>:<db_password>@cluster0.sbult9z.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)

db = client["testdb"]
collection = db["users"]

# ==========================
# Form Page
# ==========================
@app.route('/')
def home():
    return render_template('form.html')

# ==========================
# Submit Form
# ==========================
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get('name')
        age = request.form.get('age')

        if not name or not age:
            return render_template('form.html', error="All fields required")

        data = {
            "name": name,
            "age": age
        }

        collection.insert_one(data)

        # Success redirect
        return redirect(url_for('success'))

    except Exception as e:
        # Error show on same page
        return render_template('form.html', error=str(e))

# ==========================
# Success Page
# ==========================
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
