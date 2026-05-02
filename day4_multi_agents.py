from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent  
import math
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv("API_KEY")  # Get API key from environment variable

# Tool 1: Calculator
@tool
def calculator_tool(input_text: str) -> str:
    """Useful for performing mathematical calculations. 
    The input should be a math expression string, for example '2 + 2'."""
    try:
        return str(eval(input_text, {"__builtins__": None}, {"math": math}))
    except:
        return "Error in calculation"
    
# Tool 2: String Length
@tool
def string_length_tool(text: str) -> str:
    """Useful for performing counting letters of a string.
     The input should be a string, for example 'Hello World'."""
    return f"Length is {len(text)}"

# Tool 3: QA Test Case Generator
@tool
def qa_tool(feature: str) -> str:
    """Useful for generating test cases for a given feature."""
    return f"Test cases for: {feature} -> Check valid input, invalid input, edge cases"

# Tool 4: Bug Analysis
@tool
def bug_analysis_tool(text: str) -> str:
    """Useful for analyzing bugs in a given system."""
    return f"Possible bug risks in: {text} -> Null inputs, incorrect validation, performance issues"

# 2. Initialize model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=API_KEY,
    temperature=0,
    verbose=True,
    max_output_tokens=500
)

# 3. Create agent
agent = create_react_agent(
    model=llm,
    tools=[calculator_tool, string_length_tool, qa_tool]
)

# 4. Run agents
response = agent.invoke({"messages": [{"role": "user", "content": "What is (45 + 10) * 3"}]})
print(response["messages"][-1].content)
response2 = agent.invoke({"messages": [{"role": "user", "content": "How many characters are in 'Agentic AI'?"}]})
print(response2["messages"][-1].content)
response3 = agent.invoke({"messages": [{"role": "user", "content": "Generate test cases for login page"}]})
print(response3["messages"][-1].content)
response4 = agent.invoke({"messages": [{"role": "user", "content": "Analyze risks in payment system"}]})
print(response4["messages"][-1].content)