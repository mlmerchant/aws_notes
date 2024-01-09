import boto3

def find_resources_by_tags(tag_filters):
    # Create a Boto3 client for the resourcegroupstaggingapi
    client = boto3.client('resourcegroupstaggingapi')

    # Prepare the tag filter format
    tag_query = []
    for key, value in tag_filters.items():
        tag_query.append({'Key': key, 'Values': [value]})

    # Retrieve resources that match the given tag filters
    response = client.get_resources(TagFilters=tag_query)

    # Extract resource ARNs from the response
    resource_arns = [resource['ResourceARN'] for resource in response.get('ResourceTagMappingList', [])]

    return resource_arns

# Example usage
tag_filters = {'TagName1': 'Value1', 'TagName2': 'Value2'}
resources = find_resources_by_tags(tag_filters)
print(resources)
