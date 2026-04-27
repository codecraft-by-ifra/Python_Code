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
    return response.text

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
        print(f"\nGemini Response: \n{data(user_input)}")
    except Exception as e:
        print(f'An error occurred: {e}')









