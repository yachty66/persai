from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.

client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

def main_openai(messages, model="gpt-4", temperature=0.0):
    """
    executes requests to openai
    """
    completion = client.chat.completions.create(
    model=model,
    messages=messages
    # messages=[
    #     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    #     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    # ]
    )
    return completion.choices[0].message.content

