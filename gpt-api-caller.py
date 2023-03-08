#
# py .\gpt-api-caller.py "write python script for hello-world" "hello_world.py"
#

import requests
import argparse
from decouple import config

parser = argparse.ArgumentParser()
parser.add_argument("prompt")
parser.add_argument("file_name")
args = parser.parse_args()

openai_api_endpoint = "https://api.openai.com/v1/completions"
openai_api_key = config("SDK_OPENAI_API_KEY")

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + openai_api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": f"{args.prompt}",
    "max_tokens": 500,
    "temperature": 0.5
}

response = requests.post(
    openai_api_endpoint, headers=request_headers, json=request_data)

if (response.status_code == 200):
    response_text = response.json()["choices"][0]["text"]
    with open(f"{args.file_name}", "w") as file:
        file.write(response_text)
        file.close()
else:
    print(f"Request failed with status {response.status_code}")
