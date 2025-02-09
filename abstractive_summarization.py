
API_KEY=""

from google import genai

def abstractive_sum(text,summary_percentage=30):
    return gemini_summary(text,summary_percentage)

def gemini_summary(text,summary_percentage=30,api_key=API_KEY):
    
    client = genai.Client(api_key=api_key)

    text_prompt = "Summarise the following text " + str(summary_percentage) + "%: (dont add any extra text) " + text
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[{"text": text_prompt}],)

    summarised_text=response.text
    return summarised_text

