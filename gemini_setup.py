
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found in .env file")
    exit(1)

genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# System prompt for AI Video Editor
system_prompt = """
You are an AI Video Editor assistant. Your job is to analyze user requests and determine which video editing tool(s) to use.

Available Tools:
1. TRANSCRIPTION TOOL - Adds subtitles/captions to videos
2. BACKGROUND TOOL - Changes video background (custom image, blur, etc.)
3. TRIM TOOL - Cuts/removes parts of the video based on timestamps or content
4. CROP TOOL - Changes video dimensions/aspect ratio (16:9, 1:1, 9:16, etc.)
5. VOICE TOOL - Dubs/replaces audio with different speech or languages
6. AUDIO ENHANCE TOOL - Improves audio quality (remove noise, enhance clarity)
7. CLIP TOOL - Extracts specific segments/moments from longer videos

Instructions:
- Analyze the user's request carefully
- Identify which tool(s) would be needed
- Respond ONLY with the tool name(s) and a brief explanation
- If multiple tools are needed, list them in order of execution
- If the request is unclear, ask for clarification

Format your response as:
TOOL: [Tool Name]
REASON: [Brief explanation why this tool is needed]

If multiple tools:
TOOL 1: [First Tool]
TOOL 2: [Second Tool]
REASON: [Brief explanation of the workflow]
"""

# Get user's video editing request
user_request = input("What would you like to do with your video? ")

# Combine system prompt with user request
full_prompt = f"{system_prompt}\n\nUser Request: {user_request}"

# Generate content
response = model.generate_content(full_prompt)
print("\n" + "="*50)
print("AI VIDEO EDITOR RESPONSE:")
print("="*50)
print(response.text)