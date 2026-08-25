from google import genai
import sys
import os

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

prompt = sys.argv[1]

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(response.text)