from flask import Flask
from flask import jsonify
from flask import request
from ec2manager import EC2Manager

app = Flask(__name__)

# ec2manager utility object to start/stop/terminate
ec2_manager = EC2Manager()


@app.route("/create_ec2/<instance_id>")
def create_ec2(instance_id: str):
    result = ec2_manager.start(instance_id=instance_id)
    return jsonify(result)


@app.route("/stop_ec2/<instance_id>")
def create_ec2(instance_id: str):
    result = ec2_manager.stop(instance_id=instance_id)
    return jsonify(result)


@app.route("/terminate_ec2/<instance_id>")
def create_ec2(instance_id: str):
    result = ec2_manager.terminate(instance_id=instance_id)
    return jsonify(result)


app.run(host="localhost", port="8080")

