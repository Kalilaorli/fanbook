from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from os.path import join, dirname
import os

MONGODB_URI = os.environ.get(
    "mongodb+srv://kalilaorli28:kalilaorli28@cluster0.c1av8ru.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("dbsparta")

client = MongoClient(
    'mongodb+srv://kalilaorli28:kalilaorli28@cluster0.c1av8ru.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta
app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.fanmessages.insert_one(doc)
    return jsonify({'msg':'POST request!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    message_list = list(db.fanmessages.find({}, {'_id': False}))
    return jsonify({'messages': message_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)