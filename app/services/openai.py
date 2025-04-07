import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_website_content(business_type, industry):
    prompt = f"Generate homepage content for a {business_type} in the {industry} industry."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a website generator assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=300
    )
    content = response["choices"][0]["message"]["content"]
    return {
        "home": content,
        "about": f"About our {business_type}",
        "contact": "Contact us via info@example.com"
    }
