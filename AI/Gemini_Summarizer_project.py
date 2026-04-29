from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key= os.getenv("GEMINI_API_KEY"))

def data(prompt):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents= prompt
    )
    text = response.text
    Tokens = 0

    if hasattr(response, "usage_metadata"):
        Tokens = response.usage_metadata.total_token_count

    return text, Tokens


def calculate_cost(tokens):
    cost_per_1k = 0.00025
    return (tokens / 1000) * cost_per_1k

print("\n"+ "*"*46)
print("\n     Welcome to Gemini Chat Sumarizer ")
print("\n"+ "*"*46)

while True:
    user_input = input("\nEnter your Query : ")

    if (user_input.lower() == 'exit'):
        print("\nGoodbye!")
        print ("--"*150 + "\n")
        break
    try:
        reponse_text, Tokens = data(user_input)
        print(f"\nGemini Response: \n{reponse_text}")
        print(f'\nToken used: {Tokens}')
        print(f'Estimated Cost OF Tokens: {calculate_cost(Tokens):.6f}')
    except Exception as e:
        print(f'An error occurred: {e}')









