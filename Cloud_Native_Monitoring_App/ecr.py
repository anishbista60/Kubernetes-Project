import boto3

client = boto3.client('ecr')
response = client.create_repository(
    repositoryName='my_app_registry'
)
print(response['repository']['registryId'])
