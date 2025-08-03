# Amazon Bedrock AgentCore Demo

A collection of demo for [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/index.html), a service that allow us to deploy and operate highly effective agents securely, at scale using any framework and model.


## Demos Availble
1. [Basic AgentCore Runtime](./basic_runtime/README.md)
1. [Agent/Runtime + AgentCore Memory](./memory/README.md)
1. [AgentCore Code Interpreter](./code_Interpreter/README.md)


## Common Set Up

Run the following command to set up the demo.
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Additional set ups required for individual demos are avaialble in the `README` within the sub-folders.