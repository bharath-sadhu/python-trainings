#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 09:19:46 2021

@author: imak
"""
from flask import Flask,jsonify
import boto3

def starter_func(ec2_id):
    try:
        ec2 = boto3.client('ec2', region_name='us-west-2', aws_access_key_id=ACCESS_ID, aws_secret_access_key=ACCESS_KEY)
        result = ec2.start_instances(InstanceIds=[ec2_id], DryRun=False)    
        return(result)
    except Exception as x:
        return "Invalid Instace iD Entered" 

def stop_func(ec2_id):
    try:
        ec2 = boto3.client('ec2', region_name='us-west-2', aws_access_key_id=ACCESS_ID, aws_secret_access_key=ACCESS_KEY)
        result = ec2.stop_instances(InstanceIds=[ec2_id], DryRun=False)    
        return(result)
    except Exception as x:
        return "Invalid Instace iD Entered" 

def terminate_func(ec2_id):
    try:
        ec2 = boto3.client('ec2', region_name='us-west-2', aws_access_key_id=ACCESS_ID, aws_secret_access_key=ACCESS_KEY)
        result = ec2.terminate_instances(InstanceIds=[ec2_id], DryRun=False)    
        return(result)
    except Exception as x:
        return "Invalid Instace iD Entered"       

app = Flask(__name__)
@app.route("/ec2_start/<ec2_id>")
def create_ec2(ec2_id: str):
    return "<H3>Starting EC2 Instance ...</H3>"
    result = starter_func(ec2_id)
    return result

@app.route("/ec2_stop/<ec2_id>")
def stop_ec2(ec2_id: str):
    return "<H3>Stopping EC2 Instance ...</H3>"
    result = stop_func(ec2_id)
    return result

@app.route("/ec2_terminate/<ec2_id>")
def terminate_ec2(ec2_id: str):
    return "<H3>Terminating EC2 Instance ...</H3>"
    result = terminate_func(ec2_id)
    return jsonify(result)

app.run(host="localhost", port= 8080)