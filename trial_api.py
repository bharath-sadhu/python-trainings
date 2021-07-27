from flask import Flask,jsonify
from ec2manager import EC2Manager


Auth = EC2Manager()

app = Flask(__name__)
@app.route("/ec2_start/<ec2_id>")
def create_ec2(ec2_id: str):
    return "<H3>Starting EC2 Instance ...</H3>"
    result = Auth.start(ec2_id=ec2_id)
    return jsonify(result)

@app.route("/ec2_stop/<ec2_id>")
def stop_ec2(ec2_id: str):
    return "<H3>Stopping EC2 Instance ...</H3>"
    result = Auth.stop(ec2_id=ec2_id)
    return jsonify(result)

@app.route("/ec2_terminate/<ec2_id>")
def terminate_ec2(ec2_id: str):
    return "<H3>Terminating EC2 Instance ...</H3>"
    result = Auth.terminate(ec2_id=ec2_id)
    return jsonify(result)

app.run(host="localhost", port= 8080)

