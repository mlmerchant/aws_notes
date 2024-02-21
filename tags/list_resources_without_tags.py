import boto3

def get_resources_without_tags():
    # Create a session using your current credentials
    session = boto3.Session()

    # Create the client for the Resource Groups Tagging API
    tagging_client = session.client('resourcegroupstaggingapi')

    # Initialize the pagination marker and result list
    pagination_token = ''
    resources_without_tags = []

    while True:
        # Fetch a batch of resources
        response = tagging_client.get_resources(
            PaginationToken=pagination_token,
            ResourcesPerPage=100,  # Adjust based on your needs
            # No specific TagFilters here as we're fetching all resources to inspect
        )

        # Process each resource in the current batch
        for resource_tag_mapping in response.get('ResourceTagMappingList', []):
            if not resource_tag_mapping['Tags']:  # Check if the resource has no tags
                resources_without_tags.append(resource_tag_mapping['ResourceARN'])

        # Check if there's another page of results
        pagination_token = response.get('PaginationToken', '')
        if not pagination_token:
            break

    return resources_without_tags

# Example usage
resources_without_tags = get_resources_without_tags()
print(f"Resources without tags: {resources_without_tags}")
