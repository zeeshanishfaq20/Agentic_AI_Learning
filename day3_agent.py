from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain_core.prompts import PromptTemplate
from langgraph.prebuilt import create_react_agent  
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv("API_KEY")  # Get API key from environment variable


# 1. Define a tool
@tool
def calculator_tool(input_text: str) -> str:
    """Useful for performing mathematical calculations. 
    The input should be a math expression string, for example '2 + 2'."""
    try:
        return str(eval(input_text))
    except:
        return "Error in calculation"

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
    tools=[calculator_tool]
)

# 4. Run agent
response = agent.invoke({"messages": [{"role": "user", "content": "What is (45 + 10) * 3"}]})
print(response["messages"][-1].content)