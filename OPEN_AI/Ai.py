from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPEN_AI_KEY")
)

response = client.responses.create(
  model="gpt-5-nano",
  input="write 10 tools name of Ai in list form",
  store=True,
)

print(response.output_text);
