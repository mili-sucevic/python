import boto3
import json

def modify_security_group(group_id, ip_protocol, from_port, to_port, cidr_block):
    ec2 = boto3.client("ec2")
    response = ec2.authorize_security_group_ingress(
        GroupId=group_id,
        IpPermissions=[
            {
                "IpProtocol": ip_protocol,
                "FromPort": from_port,
                "ToPort": to_port,
                "IpRanges": [
                    {
                        "CidrIp": cidr_block
                    }
                ]
            }
        ]
    )
    
    print(json.dumps(response, indent=4))

modify_security_group("sg-0123456789abcdef0", "tcp", 22, 22, "0.0.0.0/0")
