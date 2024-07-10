import os
from PIL import Image
from io import BytesIO
import base64
from dotenv import load_dotenv
import google.generativeai

load_dotenv()

google.generativeai.configure(api_key=os.environ.get('API_KEY'))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = google.generativeai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=generation_config)

def get_data(file_storage):
    #img = PIL.Image.open(f"static/images/{img.filename}")
    img = Image.open(file_storage.stream)
    response = model.generate_content(["General description about dog breed in the image, including history and origin",img],stream=True)
    response.resolve()
    return response.text

def convert_image_to_base64(file_storage):
    # Convert the FileStorage object to a PIL Image object
    buffered = BytesIO()
    img = Image.open(file_storage)
    img.save(buffered, format="JPEG")
    image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return image_base64
