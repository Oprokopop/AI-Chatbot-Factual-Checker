import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def check_fact(statement):
    """Checks the factual accuracy of a statement using GPT-4."""
    prompt = f"Check the factual accuracy of the following statement and determine if it is true, false, or misleading: '{statement}'"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a factual verification assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    statement = input("Enter a statement to fact-check: ")
    result = check_fact(statement)
    print("Factual Check Result:\n", result)
