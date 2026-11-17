import os
from uuid import uuid4

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

session_id = os.getenv("OPENCODE_SESSION_ID", str(uuid4()))

model = ChatOpenAI(
    model="gpt-6-luna",
    api_key=os.getenv("OPENCODE_API_KEY"),
    base_url="https://opencode.ai/zen/go/v1",
    use_responses_api=True,
    default_headers={"x-opencode-session": session_id},
)
