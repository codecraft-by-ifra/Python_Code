# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# # Load API key
# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # 🔹 Summarize function
# def summarize_text(text):
#     response = client.chat.completions.create(
#         model="gpt-5-mini",
#         messages=[
#             {"role": "system", "content": "Summarize the given text."},
#             {"role": "user", "content": text}
#         ]
#     )

#     summary = response.choices[0].message.content
#     tokens_used = response.usage.total_tokens

#     return summary, tokens_used


# # 🔹 Cost function
# def calculate_cost(tokens):
#     cost_per_1k = 0.0003
#     return (tokens / 1000) * cost_per_1k


# # 🔹 Main program
# def main():
#     choice = input("Enter 1 for manual input OR 2 for file input: ")

#     if choice == "1":
#         text = input("\nEnter your text:\n")

#     elif choice == "2":
#         try:
#             with open("input.txt", "r", encoding="utf-8") as file:
#                 text = file.read()
#         except:
#             print("File not found!")
#             return
#     else:
#         print("Invalid choice")
#         return

#     try:
#         summary, tokens = summarize_text(text)
#         cost = calculate_cost(tokens)

#         print("\n🔹 Summary:\n", summary)
#         print(f"\n🔹 Tokens Used: {tokens}")
#         print(f"💰 Estimated Cost: ${cost:.6f}")

#     except Exception as e:
#         print("Error:", e)


# # Run program
# if __name__ == "__main__":
#     main()





import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))

def data(prompt):
    response = client.chat.completions.create(
        model= "gpt-4.1-mini",
        messages= {
            'role': 'user',
            'content': 'prompt'
        }
    )
    return response.choices[0].message.content



print("\n"+ "*"*46)
print("\n     Welcome to OpenAi Chat Sumarizer ")
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