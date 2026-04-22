from anthropic import Anthropic
import os
from dotenv import load_dotenv
load_dotenv()

client = Anthropic(
    api_key= os.getenv("ANTHROPIC_API_KEY")
    )
response = client.messages.create(
  model="claude-opus-4-7",
  system="You are a helpful assistant.",
  messages =[{
          "role": "user",
          "content":"10 names of girls with numbering"
      }],
  max_tokens=1000
)
print(response.content[0].text);
