
# API_KEY="AIzaSyApoQP0IAo6SzjtzVE_R--fA30HoWjoU24"
from dotenv import load_dotenv
import os

if os.getenv("RENDER") is None:  # Render automatically sets 'RENDER' in hosted env
    load_dotenv()

API_KEY=os.getenv("GEMINI_API_KEY")
from google import genai


def abstractive_sum(text,summary_percentage=30):
    return gemini_summary(text,summary_percentage)

def gemini_summary(text,summary_percentage=30,api_key=API_KEY):
    
    max_input_words = 1200
    words = text.split()
    
    if len(words) > max_input_words:
        text = ' '.join(words[:max_input_words])

    client = genai.Client(api_key=api_key)

    text_prompt = f"""Summarize the following text to approximately {summary_percentage} % Percentage of its original length {len(text.split())}. 
    Keep the key points clear and maintain the original meaning.
    original text : {text}

    Use the following format for the summary:

    Summary:
    "[Summarized text here]"

    Key Points:
    - Point 1
    - Point 2
    - Point 3
    - Point 4
    """ 

    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[{"text": text_prompt}],)

    summarised_text=response.text
    return summarised_text.replace('Summary:','')

