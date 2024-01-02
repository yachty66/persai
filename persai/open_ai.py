from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()  

client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

def main_openai(messages, model="gpt-4", temperature=0.0):
    """
    Executes requests to OpenAI.
    """
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return completion.choices[0].message.content

