# Basic AgentCore Runtime Demo

A Basic Example on Using AgentCore Runtime with OpenAI agent.

For details, please refer to my blog: [Amazon Bedrock AgentCore. Part 1: Overview + Runtime Dive!]()

## Set Up & Deploy
Make sure that the working directory is the `basic_runtime` directory and perform the following steps.

1. set up `OPENAI_API_KEY` in [basic_runtime.py](./basic_runtime.py)
2. Start docker or Finch
3. Sign in through the AWS Command Line Interface and make sure the credentials are valid
4. Configure the agent with `agentcore configure --entrypoint basic_runtime.py --region us-east-1`
    - ECR repository and IAM role with [required permissions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html) can be created automatically with this command and thus set up prior to deployment is not required.
    - This command will generate a `Dockerfile`, a `.dockerignore`, and a `.bedrock_agentcore.yaml` configuration file
    - `region` parameter is required if the default region is not one of the [regions AgentCore supported](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html)
5. Deploy the agent to the cloud as a Runtime with `agentcore launch`
    - This command will Build the Docker image, Create an ECR repository and an IAM Role if we have specified auto creation when running the configure command, Push the image to ECR, Create a Bedrock AgentCore runtime, Deploy the agent to the cloud, and If we had auto-creation for ECR or IAM Role, the .bedrock_agentcore.yaml will be updated. Specially, the `execution_role` will contain the arn for newly created role, `execution_role_auto_create` will be set to `false`, `ecr_repository` will contain the URI for the ECR repository created, and `ecr_auto_create` will be set to `false`.


## Invocation
To invoke the agent deployed above,
1. With CLI: `agentcore invoke '{"prompt": "tell me about pikachu"}'`
    - Above command needs to be ran within the the `basic_runtime` directory, ie: the directory containing `.bedrock_agentcore.yaml`.
2. With SDK: refer to the [`invoke_demo.ipynb`](./invoke_demo.ipynb) notebook