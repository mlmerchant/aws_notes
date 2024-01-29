import boto3

# Initialize a session using Amazon SSM
ssm_client = boto3.client('ssm', region_name='your_region')

# Get a list of all managed instances
response = ssm_client.describe_instance_information()
all_instance_ids = [instance['InstanceId'] for instance in response['InstanceInformationList']]

# Get a list of all patch groups
response = ssm_client.describe_patch_groups()
all_patch_groups = list(response['Mappings'].keys())

# Initialize a set to store instances associated with patch groups
instances_with_patch_groups = set()

# Loop through all patch groups and get instances associated with them
for patch_group in all_patch_groups:
    response = ssm_client.list_association_versions(
        AssociationName='AWS-RunPatchBaseline',
        MaxResults=50,  # Adjust this as needed to retrieve all instances
        Filters=[
            {
                'Key': 'PatchGroup',
                'Values': [patch_group],
            },
        ],
    )
    instances_with_patch_groups.update(instance['InstanceId'] for version in response['AssociationVersions'])

# Calculate instances without patch group associations
instances_without_patch_groups = set(all_instance_ids) - instances_with_patch_groups

# Print the count of instances without patch group associations
print(f"Number of instances without patch group associations: {len(instances_without_patch_groups)}")
