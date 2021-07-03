#!/usr/bin/python
# -*- coding: latin-1 -*-
from flask import Flask, request, json, jsonify
import redis
HOST = "localhost"
PORT = 8007
SUBSCRIPTION_LIST = "MYLIST"
redisClient = redis.Redis(host='localhost', port=6379, db=0)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/save', methods=['POST'])
def register():
    # print(request.data)
    data = request.json
    # print("sasas",data)
    # email = request.data.get('email')
    # name = request.data.get('name')
    redisClient.rpush(SUBSCRIPTION_LIST, data)

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
    list = redisClient.lrange(SUBSCRIPTION_LIST,0 ,-1)
    print(list)
    response = app.response_class(
        response=json.dumps({"message": "Success", "status": 1}),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(HOST, PORT, True)
