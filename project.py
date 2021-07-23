from flask import Flask
from flask import jsonify
from flask import request
from datetime import datetime
import pytz
utc=pytz.UTC
import boto3
import logging

app = Flask(__name__)
client = boto3.client('s3')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/buckets", methods=["GET"])
def getBuckets():
    buckets = client.list_buckets()
    print(buckets)
    return jsonify(buckets['Buckets']), 200

@app.route("/buckets/<bucketName>", methods=["GET"])
def getBucketInfo(bucketName):
    buckets = client.list_buckets()
    print(buckets)
    for bucket in buckets['Buckets']:
        if bucket['Name'] == bucketName:
            return jsonify(bucket), 200
    return jsonify("Could not find bucket with name {0}".format(bucketName)), 400

@app.route("/bucket", methods=["GET"])
def getBucketInfoWithQueryParams():
    bucketName = request.args.get("id")
    if "start" in request.args:
        logging.info(request.args.get("start"))
        startDate = datetime.strptime(request.args.get("start"), "%d-%m-%Y")
    else:
        startDate = None
    if "end" in request.args:
        endDate = datetime.strptime(request.args.get("end"), "%d-%m-%Y")
    else:
        endDate = None
    buckets = client.list_buckets()
    if bucketName != None:
        print(buckets)
        for bucket in buckets['Buckets']:
            if bucket['Name'] == bucketName:
                return jsonify(bucket), 200
        return jsonify("Could not find bucket with name {0}".format(bucketName)), 400
    elif startDate != None and endDate != None:
        allBucketsBetweenStartAndEnd = []
        for bucket in buckets['Buckets']:
            bucketCreationTime = bucket['CreationDate']
            if bucketCreationTime >= utc.localize(startDate) and bucketCreationTime < utc.localize(endDate):
                allBucketsBetweenStartAndEnd.append(bucket)
        if len(allBucketsBetweenStartAndEnd) > 0:
            return jsonify(allBucketsBetweenStartAndEnd), 200
        return jsonify("Could not find bucket with provided criteria"), 400

app.run(host="localhost", port=8080)
