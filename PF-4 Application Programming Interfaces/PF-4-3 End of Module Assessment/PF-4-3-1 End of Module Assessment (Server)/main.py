from flask import Flask, jsonify, request
from threading import Thread
from replit import db

app = Flask('')


@app.route('/')
def home():
  return "Cheep!"


@app.route('/send_cheep', methods=['POST'])
def send_cheep():
  db[request.get_json()["message"]] = ""
  return jsonify({"cheep?": "cheep!"})


@app.route('/get_cheeps', methods=['GET'])
def get_cheeps():
  return jsonify(list(db.keys()))


def run():
  app.run(host='0.0.0.0', port=7000)


t = Thread(target=run)
t.start()
