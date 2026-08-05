from llm.client import LLMClient
from config import (
    API_KEY,
    API_BASE_URL,
    MODEL_NAME
)


client = LLMClient(
    API_KEY,
    API_BASE_URL,
    MODEL_NAME
)


response = client.generate(
    "Explain binary search in one sentence."
)


print(response)
