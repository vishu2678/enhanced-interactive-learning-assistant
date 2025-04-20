import time
from openai import OpenAI, RateLimitError

client = OpenAI()

def get_academic_content(topic):
    retries = 5
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're an academic research assistant."},
                    {"role": "user", "content": f"Give academic content on {topic}"}
                ],
                max_tokens=300
            )
            return response.choices[0].message.content
        except RateLimitError as e:
            print(f"Rate limit hit (attempt {attempt+1}/{retries}): {e}")
            time.sleep(2 ** attempt)  # exponential backoff
        except Exception as e:
            print(f"Unhandled error: {e}")
            break
    return "Error fetching academic content. Please try again later."



