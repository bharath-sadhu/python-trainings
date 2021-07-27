import boto3


class EC2Manager:
    """ EC2 manager class to start/stop/terminate ec2 instances
    """

    def __init__(self):
        self.ec2 = boto3.client('ec2')  # ec2 client
        self.instance_info = {}  # dictionary storing temporary instance info

    def start(self, instance_id):
        """
        start an ec2 instance with an instance id
        :param instance_id:
        :return: response
        """
        try:
            if instance_id in self.instance_info and self.instance_info[instance_id] == "running":
                return "Instance already started"
            else:
                response = self.ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
                self.instance_info[instance_id] = "running"
                return response
        except Exception as e:
            return e

    def stop(self, instance_id):
        """
        stop an ec2 instance with an instance id
        :param instance_id:
        :return:
        """
        try:
            if instance_id in self.instance_info and self.instance_info[instance_id] == "stopped":
                return "Instance already stopped"
            else:
                response = self.ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
                self.instance_info[instance_id] = "stopped"
                return response
        except Exception as e:
            return e

    def terminate(self, instance_id):
        """
        terminate an ec2 instance with an instance id
        :param instance_id:
        :return:
        """
        try:
            if instance_id in self.instance_info:
                response = self.ec2.terminate_instances(InstanceIds=[instance_id],DryRun=False)
                self.instance_info.pop(instance_id)
                return response
            else:
                return "No instance found"
        except Exception as e:
            return e

    def describe(self):
        """
        return all instances present
        :return:
        """
        try:
            response = self.ec2.describe_instances(
                Filters=[
                    {
                        'Name': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
            )
            return response
        except Exception as e:
            return e
