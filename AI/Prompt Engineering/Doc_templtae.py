import json
from datetime import datetime

# =============================================
# Prompt Documentation — aaj ke best prompts
# =============================================

prompt_library = {
    "version": "1.0",
    "date": datetime.now().strftime("%Y-%m-%d"),
    "prompts": [

        {
            "id": 1,
            "category": "code_generation",
            "technique": "role + constraints",
            "task": "Write Python function",
            "bad_prompt": "Write code to check palindrome",
            "good_prompt": "Act as a senior Python developer. Write a function is_palindrome(s) that checks if string s is a palindrome. Include: type hints, docstring, handle edge cases (empty string, None), 3 test cases.",
            "why_better": "Role activates expertise. Constraints give exact output needed.",
            "rating": 5
        },

        {
            "id": 2,
            "category": "explanation",
            "technique": "audience + format",
            "task": "Explain API",
            "bad_prompt": "What is an API?",
            "good_prompt": "Explain what an API is to a 12-year-old who loves ordering food online. Use a food delivery app analogy. Max 3 sentences.",
            "why_better": "Audience + analogy = memorable, simple explanation.",
            "rating": 5
        },

        {
            "id": 3,
            "category": "data_extraction",
            "technique": "output format",
            "task": "Extract data as JSON",
            "bad_prompt": "Extract name and age",
            "good_prompt": "Extract information and return ONLY valid JSON, no explanation, no markdown:\nText: {text}\nFormat: {\"name\": \"\", \"age\": 0, \"city\": \"\"}",
            "why_better": "Format control = parseable output in code. No extra text.",
            "rating": 5
        },

        {
            "id": 4,
            "category": "reasoning",
            "technique": "chain-of-thought",
            "task": "Math/logic problems",
            "bad_prompt": "Solve: 15% of 840 = ?",
            "good_prompt": "Solve step by step:\n15% of 840 = ?\nShow each calculation clearly.",
            "why_better": "CoT reduces errors in calculations. Steps visible = verifiable.",
            "rating": 4
        },

        {
            "id": 5,
            "category": "creative",
            "technique": "constraints + tone",
            "task": "Write professional email",
            "bad_prompt": "Write an email",
            "good_prompt": "Write a professional email to reschedule a meeting. Tone: apologetic but confident. Length: under 70 words. Include: subject line, reason (family emergency), proposed new time.",
            "why_better": "Constraints prevent AI from writing a 500-word essay.",
            "rating": 5
        }
    ],

    "key_learnings": [
        "Vague prompts = vague output. Always be specific.",
        "Role + Task + Format = best combo for structured output.",
        "Chain-of-thought helps with logic and math tasks.",
        "Few-shot examples work best for pattern-based tasks.",
        "Temperature 0 for factual tasks, 0.7+ for creative."
    ]
}

# Save karo
with open("prompt_log.json", "w") as f:
    json.dump(prompt_library, f, indent=2)

print("Prompt library saved to prompt_log.json")
print(f"Total prompts logged: {len(prompt_library['prompts'])}")
print("\nKey learnings:")
for i, l in enumerate(prompt_library['key_learnings'], 1):
    print(f"  {i}. {l}")