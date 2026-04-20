from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
Question = [
    "What is Artificial Intelligence?", 
    "What are the advantages of Artificial Intelligence?",
    "What are the disadvantages of Artificial Intelligence?"
]
    
for i in Question:
    response = client.responses.create(
        model="gpt-5-nano",
        input= "Give very short answer (max 2-3 lines): " + i,
        store=True
    )
    answer = response.output_text
    if not answer:
        answer = "No answer found."
    print("\nQ:", i)
    print("A:", answer)
    print("-" * 50)
