
# Configure OpenAI Agent
import uuid
from agents import set_default_openai_key, Agent, Runner, RunResult, TResponseInputItem

OPENAI_API_KEY="sk-..."
set_default_openai_key(OPENAI_API_KEY)

# memory id for the memory (database) to be used with the agent
# can be created by going through the create_memory.ipynb notebook
memory_id = "PokemonAgentMemory-zCM04KDWbq"

pokemon_agent = Agent(
    name="Pokemon agent",
    instructions="You are specialized in pokemons. Your job is to help user understanding pokemon types and choosing the correct pokemon to use in pokemon battle.",
    model="gpt-4o-mini"
)

from bedrock_agentcore.memory import MemoryClient
client = MemoryClient(region_name="us-east-1")


async def create_agent_input(user_id: str, session_id: str, query: str) -> list[TResponseInputItem]:
    # short-term memories
    events = client.list_events(
        memory_id=memory_id,
        actor_id=user_id,
        session_id=session_id,
        max_results=5,
    )
    history: list[TResponseInputItem] = [
        {
            "role": item["conversational"]["role"].lower(),
            "content": item["conversational"]["content"]["text"],
            "type": "message"
        }
        for event in sorted(events, key=lambda x: x["eventTimestamp"])
        for item in event["payload"]
    ]

    history.append({"role": "user", "content": query, "type": "message"})

    # long term memories
    summaries = client.retrieve_memories(
        memory_id=memory_id,
        # modifie namespace if necessary, to match that of the strategy.
        namespace=f"/summaries/{user_id}/{session_id}",
        query="Summarize the past conversations.", # sumamrize based on the user input
        top_k = 1 # top score summarization only
    )

    if len(summaries) > 0:
        summary = summaries[0]["content"]["text"]
        history.insert(0, {"role": "developer", "content": f"Here is a summarization of the past conversation. {summary}", "type": "message"})

    return history

# save the new conversation to memory
async def save_memory(user_query: str, assistant_answer: str, session_id: str, user_id: str):
    client.create_event(
        memory_id=memory_id,
        actor_id=user_id,
        session_id=session_id,
        messages=[
            (user_query, "USER"),
            (assistant_answer, "ASSISTANT"),
        ],
    )


# Integration with Bedrock AgentCore
from bedrock_agentcore.runtime import BedrockAgentCoreApp

# Initialize the app
app = BedrockAgentCoreApp()

# define entry point
@app.entrypoint
async def agent_invocation(payload, context):
    print(f"payload: {payload}")

    # assuming the JSON Payload user sent contains key: prompt, user_id, session_id
    query = payload.get("prompt", "Tell me about pokemon?")
    user_id = payload.get("user_id", "user_unknwon")

    # not using context.session_id
    # because when we create a new memory, we will need a session_id,
    # however, at this point, the session_id is not available yet to the caller and cannot be specified when invoking
    session_id = payload.get("session_id", str(uuid.uuid4()))
    try:
        messages = await create_agent_input(user_id=user_id, session_id=session_id, query=query)
        result = await Runner.run(pokemon_agent, input=messages)
        await save_memory(user_query=query, assistant_answer=result.final_output, session_id=session_id, user_id=user_id)
        return {
            "result": result.final_output,
            "session_id": session_id,
            "user_id": user_id,
        }
    except Exception as e:
        print(f"Error during agent execution: {e}")
        return {"result": f"Error: {str(e)}"}


# Run the app
if __name__== "__main__":
    app.run()