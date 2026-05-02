from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv("API_KEY")  # Get API key from environment variable

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text="""You are a senior QA engineer. 
Generate 3 test cases for a login page in this JSON format:
[
  {
    "test_case": "",
    "steps": [],
    "expected_result": ""
  }
]"""
                ),
            ],
        ),
    ],
    config=types.GenerateContentConfig(
        temperature=0,       # Keep it factual and stable
        max_output_tokens=500, # Limit response to ~400 words
        top_p=0.95,            # Nucleus sampling (optional)
        stop_sequences=["END"] # Force stop if it writes "END"
    )
)

print(response.text)