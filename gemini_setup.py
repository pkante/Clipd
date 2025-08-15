import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize model
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Test the connection
response = model.generate_content("Hello, Gemini!")
print(response.text)