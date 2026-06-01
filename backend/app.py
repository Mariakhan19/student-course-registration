from flask import Flask,request,jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://mongodb:27017")

db = client["studentDB"]

collection = db["students"]

@app.route("/register",methods=["POST"])
def register():

    data = request.json

    collection.insert_one(data)

    return jsonify({
        "message":"Student Registered Successfully"
    })

app.run(host="0.0.0.0",port=5001)