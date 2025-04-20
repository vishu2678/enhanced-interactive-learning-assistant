import time
from openai import OpenAI, OpenAIError, RateLimitError

client = OpenAI(api_key="your-api-key")  # Replace with your actual key or use environment variable

def get_web_content(topic):
    retries = 5
    delay = 5  # Start with 5 seconds

    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Give me a summary of {topic}"}],
                max_tokens=300
            )
            return response.choices[0].message.content

        except RateLimitError:
            print(f"[Rate Limit] Retry {attempt + 1}/{retries}. Waiting for {delay}s...")
            time.sleep(delay)
            delay *= 2  # Exponential backoff

        except OpenAIError as e:
            print(f"[OpenAI Error] {e}")
            break

    return "Sorry, could not fetch content due to rate limits. Please try again later."


