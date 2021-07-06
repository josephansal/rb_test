#!/usr/bin/python
# -*- coding: latin-1 -*-
from os import confstr
from flask import Flask, request, json, jsonify
import redis
from flask_cors import CORS
import json
# Import smtplib for the actual sending function
import smtplib

# And imghdr to find the types of our images
import imghdr

# Here are the email package modules we'll need
from email.message import EmailMessage

HOST = "localhost"
PORT = 8007
SUBSCRIPTION_LIST = "MYLIST"
redisClient = redis.Redis(host='localhost', port=6379, db=0)
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/save', methods=['POST'])
def register():
    data = request.json
    with open('data.json', 'w') as tfile:
        json.dump([data], tfile, ensure_ascii=False, indent=4)
    # with open('data.json', 'w', encoding='utf-8') as f:
    # json.dump(data, f, ensure_ascii=False, indent=4)
    response = app.response_class(
        response=json.dumps({"message": "Success", "status": 1}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/export', methods=['POST'])
def export():
    return 'export list'


@app.route('/list')
def list():
    f = open('data.json')
    data = json.load(f)
    print(data)
    # data = [{"sl":"1", "name": "John", "email":"john@sasa.com"}]
    response = app.response_class(
        response=json.dumps(
            {"message": "Success", "status": 1, "data": json.dumps(data)}),
        status=200,
        mimetype='application/json'
    )
    return response


def send_email(email):

    # Create the container email message.
    msg = EmailMessage()
    msg['Subject'] = 'News letter'
    # me == the sender's email address
    # family = the list of all recipients' email addresses
    msg['From'] = "josephansal@gmail.com"
    msg['To'] = email
    msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # Open the files in binary mode.  Use imghdr to figure out the
    # # MIME subtype for each specific image.
    # for file in pngfiles:
    #     with open(file, 'rb') as fp:
    #         img_data = fp.read()
    #     msg.add_attachment(img_data, maintype='image',
    #                        subtype=imghdr.what(None, img_data))

    # Send the email via our own SMTP server.
    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)


if __name__ == '__main__':
    app.run(HOST, PORT, True)
