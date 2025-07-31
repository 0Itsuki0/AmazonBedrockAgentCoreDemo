# AgentCore Memory Demo

A AgentCore Runtime with OpenAI agent using AgentCore memory for conversation history and summary.

For more details or other potential use cases beyond Runtime/Agent (independently as a Database), please refer to my blog: [Bedrock AgentCore Part2: Memory. Raw Database + Vector store + Some EventBridge-ish Logics!]()


## Set Up & Deploy
1. Create Memory (resource) using [`create_memory.ipynb`](./docs/create_memory.ipynb). This will both enable the short-term and long-term memory. Note down the memory id.
2. Set up `OPENAI_API_KEY` and `memory_id` in [basic_runtime.py](./runtime_with_memory.py)
3. Configure and deploy the Agent Runtime. For more details, refer to [basic_runtime](../basic_runtime/README.md)
4. Set up execution role permission using the [add_role_permission.ipynb](./docs/add_role_permission.ipynb) notebook. By default, the IAM role created with agentCore deploy command will not have permissions to access AgentCore Memory-related resources.


In addition, to get an idea of how memory manipulations works, save and store short-term memories, retrieving long-term memories, branching, and etc, please refer to the [working_with_memory.ipynb](./docs/working_with_memory.ipynb) notebook.


## Invocation
Refer to the [`invoke_demo.ipynb`](./docs/invoke_demo.ipynb) notebook for invocation demo and necessary parameters when creating the payload.