from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver  
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv("API_KEY")  # Get API key from environment variable


# 1. Define a tool
@tool
def echo_tool(text: str) -> str:
    """Useful for echoing back the input text."""
    return f"You said: {text}"

# 2. Memory
Memory = InMemorySaver()

# 2. Initialize model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=API_KEY,
    temperature=0,
    verbose=True
)

# 3. Create agent
agent = create_react_agent(
    model=llm,
    tools=[echo_tool],
    checkpointer=Memory
)

# 5. Run agent with a 'thread_id' to enable memory persistence
config = {"configurable": {"thread_id": "unique_session_id_123"}}

# 6. Run agent
response = agent.invoke({"messages": [{"role": "user", "content": "My name is Ash"}]}, config=config)
print(response["messages"][-1].content)
response = agent.invoke({"messages": [{"role": "user", "content": "What is my name?"}]}, config=config)
print(response["messages"][-1].content)