from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import SecretStr
import os

load_dotenv()

# Load the key from .env
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in .env file")

# Wrap it in SecretStr to satisfy type checker
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=SecretStr(api_key)  # <-- this removes the warning
)

if __name__ == "__main__":
    response = llm.invoke("What are the two main ingredients in chocolate cake?")
    print(response.content)
