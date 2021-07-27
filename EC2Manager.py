#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 18:45:13 2021

@author: imak
"""

import boto3


class EC2Manager:

    def __init__(self):
        self.ec2 = boto3.client('ec2')  
        self.instance_info = {}  

    def start(self, ec2_id):
        try:
            if ec2_id in self.instance_info and self.instance_info[ec2_id] == "running":
                return "Instance already running"
            else:
                result = self.ec2.start_instances(InstanceIds=[ec2_id], DryRun=False)
                self.instance_info[ec2_id] = "running state"
                return result
        except Exception as x:
            return x

    def stop(self, ec2_id):
        try:
            if ec2_id in self.instance_info and self.instance_info[ec2_id] == "stopped":
                return "Instance already stopped"
            else:
                response = self.ec2.stop_instances(InstanceIds=[ec2_id], DryRun=False)
                self.instance_info[ec2_id] = "stopped state"
                return response
        except Exception as x:
            return x

    def terminate(self, ec2_id):
        try:
            if ec2_id in self.instance_info:
                response = self.ec2.terminate_instances(InstanceIds=[ec2_id],DryRun=False)
                self.instance_info.pop(ec2_id)
                return response
            else:
                return "No instance found"
        except Exception as x:
            return x

 