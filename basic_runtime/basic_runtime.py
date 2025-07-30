
# Configure OpenAI Agent
from agents import set_default_openai_key, Agent, Runner, RunResult

OPENAI_API_KEY="sk-..."
set_default_openai_key(OPENAI_API_KEY)

pokemon_agent = Agent(
    name="Pokemon agent",
    instructions="You are specialized in pokemons. Your job is to help user understanding pokemon types and choosing the correct pokemon to use in pokemon battle.",
    model="gpt-4o-mini"
)


# Integration with Bedrock AgentCore
from bedrock_agentcore.runtime import BedrockAgentCoreApp

# Initialize the app
#
# BedrockAgentCoreApp behind the scenes
# When we use BedrockAgentCoreApp, it automatically:
#
# - Creates an HTTP server that listens on port 8080
# - Implements the required /invocations endpoint for processing requests
# - Implements the /ping endpoint for health checks
# - Handles proper content types and response formats
# - Manages error handling according to AWS standards
app = BedrockAgentCoreApp()

# define entry point
@app.entrypoint
async def agent_invocation(payload, context):
    print(f"Received payload: {payload}")
    # assuming the JSON Payload user sent is in the format '{"prompt": "{some_input}"}'
    query = payload.get("prompt", "Help me to find a pokemon for battling.")

    try:
        result = await Runner.run(pokemon_agent, query)
        return {"result": result.final_output}
    except Exception as e:
        print(f"Error during agent execution: {e}")
        return {"result": f"Error: {str(e)}"}


# Run the app
if __name__== "__main__":
    app.run()