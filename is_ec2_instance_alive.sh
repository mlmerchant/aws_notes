#!/bin/bash

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null
then
    echo "AWS CLI not installed. Please install it and configure your credentials."
    exit 1
fi

# Check if instance ID is provided
if [ $# -eq 0 ]
then
    echo "Usage: $0 <instance-id>"
    exit 1
fi

INSTANCE_ID=$1

# Check the status of the instance
instance_status=$(aws ec2 describe-instance-status --instance-ids $INSTANCE_ID --query 'InstanceStatuses[0].InstanceState.Name' --output text)

# Check if the command was successful
if [ $? -ne 0 ]; then
    echo "Failed to retrieve the status of the instance. Make sure the instance ID is correct and you have the necessary permissions."
    exit 1
fi

# Output the status
if [ "$instance_status" = "running" ]; then
    echo "Instance $INSTANCE_ID is online."
else
    echo "Instance $INSTANCE_ID is not online. Current status: $instance_status"
fi
