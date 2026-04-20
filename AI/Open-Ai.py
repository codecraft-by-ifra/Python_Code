from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
  model="gpt-5-nano",
  input="write 10 tools name of Ai",
  store=True,
  max_output_tokens=1000

)
print(response.output_text);
