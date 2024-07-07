import os
import PIL.Image
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ.get('API_KEY'))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=generation_config)

def get_data(img):
    img = PIL.Image.open(f"static/images/{img.filename}")
    response = model.generate_content(["General description about dog breed in the image, including history and origin",img],stream=True)
    response.resolve()
    return response.text
