import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash-lite")

print("AI Chatbot Ready (type exit to stop)")
while True:
 user_input = input("You: ")
 if user_input.lower() == "exit":
  break
 response = model.generate_content(user_input)
 print("AI:", response.text)