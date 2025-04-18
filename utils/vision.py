from openai import OpenAI
import os
from PIL import Image
import base64

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_image(image_path):
    # Encode image to base64
    with open(image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",  # ✅ New supported model
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this car photo for social media context."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content
