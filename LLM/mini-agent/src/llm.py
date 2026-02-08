
import os
from dotenv import load_dotenv

load_dotenv()

# ---------- OpenAI ----------
from openai import OpenAI
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def openai_llm(prompt):
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# ---------- Gemini ----------
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def gemini_llm(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
