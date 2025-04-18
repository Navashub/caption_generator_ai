from openai import OpenAI
import os
from utils.prompts import caption_prompt_template

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_caption_pack(image_description):
    prompt = caption_prompt_template.format(description=image_description)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    output = response.choices[0].message.content

    
    lines = output.strip().split("\n")
    caption = lines[0].replace("Caption:", "").strip()
    hashtags = [tag.strip() for tag in lines[1].replace("Hashtags:", "").split()]
    sounds = []
    for line in lines[2:]:
        if line.startswith("-"):
            if "–" in line:
                title, vibe = line[2:].split("–")
                sounds.append({"title": title.strip(), "vibe": vibe.strip()})

    return {
        "caption": caption,
        "hashtags": hashtags,
        "sounds": sounds
    }
