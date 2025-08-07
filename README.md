# Amazon Bedrock AgentCore Demo

A collection of demo for [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/index.html), a service that allow us to deploy and operate highly effective agents securely, at scale using any framework and model.


## Demos Availble

### AgentCore Basics
1. [Basic AgentCore Runtime](./basic_runtime/README.md)
2. [Agent/Runtime + AgentCore Memory](./memory/README.md)
3. [AgentCore Code Interpreter](./code_Interpreter/README.md)
4. [AgentCore Browser](./browser/README.md)
5. [AgentCore Gateway](./gateway/gateway_demo.ipynb)


### A Little Advance
1. [Browser Task Automation (A simple Nova-act alternative)](./advance_usages/browser_automation.ipynb)



## Common Set Up

Run the following command to set up the demo.
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Additional set ups required for individual demos are avaialble in the `README` within the sub-folders.