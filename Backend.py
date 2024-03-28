from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
# client = MongoClient('mongodb://mongo:27017/')
# db = client.webapp_db

@app.route('/register', methods=['POST'])
def register():
    user_data = request.json
    # db.users.insert_one(user_data)
    return jsonify({"message": "User registered successfully!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
