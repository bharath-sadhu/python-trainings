## Imports
from flask import Flask,request,render_template
import boto3

## Open File containing credentials
with open('/Users/jeebu_aa/Downloads/Admin_accessKeys.txt', newline='') as f:
    ACCESS_ID=f.readline()
    ACCESS_ID=ACCESS_ID[:-1]
    ACCESS_KEY=f.readline()

def ec2_func(fun,inst_id):
    try:
        ec2 = boto3.client('ec2', region_name='us-west-2', aws_access_key_id=ACCESS_ID, aws_secret_access_key=ACCESS_KEY)
        if fun=="started":
            response = ec2.start_instances(InstanceIds=[inst_id], DryRun=False)
        elif fun=="stopped":
            response = ec2.stop_instances(InstanceIds=[inst_id], DryRun=False)
        elif fun=='terminated':
            response = ec2.terminate_instances(InstanceIds=[inst_id], DryRun=False)
        return 'Instance with ID: '+inst_id+' has been '+fun.upper()
    except ClientError as e:
        return 'Invalid Instance ID'


app=Flask(__name__)


## Main Page
@app.route('/', methods=['GET'])
def main():
    h1="<H1>Main Page</H1>"
    start='<a href="/start" style="display: block;">Start Instance</a>'
    stop='<a href="/stop" style="display: block;">Stop Instance</a>'
    terminate='<a href="/terminate" style="display: block;">Terminate Instance</a>'
    return h1+start+stop+terminate

## Start EC2 Page
@app.route('/start', methods=['GET'])
def start_form():
    a = "<H1>Start EC2</H1>"
    return a + render_template('form-template.html')

@app.route('/start', methods=['POST'])
def start_form_post():
    instance_id = request.form['text']
    show = ec2_func('started', instance_id)
    return show


## Stop EC2 Page
@app.route('/stop', methods=['GET'])
def stop_form():
    a= "<H1>Stop EC2</H1>"
    return a + render_template('form-template.html')

@app.route('/stop', methods=['POST'])
def stop_form_post():
    instance_id = request.form['text']
    show = ec2_func('stopped',instance_id)
    return show


## Terminate EC2 Page
@app.route('/terminate', methods=['GET'])
def terminate_form():
    a= "<H1>Terminate EC2</H1>"
    return a + render_template('form-template.html')

@app.route('/terminate', methods=['POST'])
def terminate_form_post():
    instance_id = request.form['text']
    show = ec2_func('terminated', instance_id)
    return show


app.run(host='localhost',port="8080")