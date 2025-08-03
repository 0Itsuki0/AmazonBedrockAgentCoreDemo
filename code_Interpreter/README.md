# Basic AgentCore Runtime Demo

A Basic Example on Using AgentCore Code Interpreter.

For details, please refer to my blog: [Bedrock AgentCore Part 3: Code Interpreter Beyond Code Execution!]()

## Demos Included
1. [Basic usage](./basic_usage.ipynb)
    - Code Execution
    - Shell Interactions
    - File System Management
2. [Agent Intergration](./agent_intergration.ipynb)
    - Intergration with OPENAI Agent as a Funtional Tool
    - To host the agent using AgentCore Runtime, please refer to [basic_runtime](../basic_runtime/README.md). Also make sure to add necessary permissions, `StartCodeInterpreterSession`, `InvokeCodeInterpreter`, `StopCodeInterpreterSession`, and etc. to the runtime Execution role similar to what we had in [memory](../memory/README.md).
3. [Code Interpreter in Public Environment](./public_environment.ipynb)
    - Create a code interpreter that execute in public environement with internet access
    - Run some code that contains HTTP request for testing
    - Stop all the running session and delete the code interpreter
4. ⭐ [Access Other AWS Resources From Code Interpreter](./access_other_aws_resource.ipynb)
    - CloudWatch Logs as an example
    - With Both terminal command as well as SDK (boto3)



In addition, there is also the [interpreter_spec](./interpreter_spec.ipynb) notebook for running some terminal commands to get some specifications of the code interpreter such as
- the running system,
- available shell commands
- python and pip version
- python libraries installed
