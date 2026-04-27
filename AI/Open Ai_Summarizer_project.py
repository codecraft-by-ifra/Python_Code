from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔹 Summarize function
def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "Summarize the given text."},
            {"role": "user", "content": text}
        ]
    )

    summary = response.choices[0].message.content
    tokens_used = response.usage.total_tokens

    return summary, tokens_used


# 🔹 Cost function
def calculate_cost(tokens):
    cost_per_1k = 0.0003
    return (tokens / 1000) * cost_per_1k


# 🔹 Main program
def main():
    choice = input("Enter 1 for manual input OR 2 for file input: ")

    if choice == "1":
        text = input("\nEnter your text:\n")

    elif choice == "2":
        try:
            with open("input.txt", "r", encoding="utf-8") as file:
                text = file.read()
        except:
            print("File not found!")
            return
    else:
        print("Invalid choice")
        return

    try:
        summary, tokens = summarize_text(text)
        cost = calculate_cost(tokens)

        print("\n🔹 Summary:\n", summary)
        print(f"\n🔹 Tokens Used: {tokens}")
        print(f"💰 Estimated Cost: ${cost:.6f}")

    except Exception as e:
        print("Error:", e)


# Run program
if __name__ == "__main__":
    main()