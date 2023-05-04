import boto3
ecr_client=boto3.client('ecr')
repo="my_repo"
response=ecr_client.create_repository(repositoryName=repo)

repository_uri=response['repository']['repositoryUri']

print(repository_uri)