from kubernetes import client,config
config.load_kube_config()

api_client=client.ApiClient()
# Define the deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="spam-detect-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "spam-detect-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "spam-detect-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="spam-detect-container",
                        image="345824897256.dkr.ecr.us-east-2.amazonaws.com/project_repo:latest",
                        ports=[client.V1ContainerPort(container_port=8501)]
                    )
                ]
            )
        )
    )
)

# Create the deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

# Define the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="spam-detect-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "spam-detect-app"},
        ports=[client.V1ServicePort(port=8501)]
    )
)

# Create the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)