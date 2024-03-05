#from dotenv import load_dotenv
import os
from openai import openai

#load_dotenv()

openai.api_type = "azure"
openai.api_base = "https://firstazureopenai05022024.openai.azure.com/"
openai.api_version = "2024-02-15-preview"
openai.api_key ="55457392c21046e8bf4223a6dac91316" # os.getenv("OPENAI_API_KEY") 

def get_completion_from_messages(system_message, user_message, model="test", temperature=0, max_tokens=500) -> str:

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{user_message}"}
    ]
    client = openai()
    response = client.Completion.create(
        engine=model,
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    
    return response.choices[0].message["content"]

if __name__ == "__main__":
    system_message = "You are a helpful assistant"
    user_message = "Hello, how are you?"
    print(get_completion_from_messages(system_message, user_message))