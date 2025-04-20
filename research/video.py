import time
from openai import OpenAI, RateLimitError, OpenAIError

client = OpenAI()

def get_video_content(topic):
    retries = 5
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're a video script researcher."},
                    {"role": "user", "content": f"Give a list of 3 YouTube video summaries or recommendations on {topic}"}
                ],
                max_tokens=300
            )
            return response.choices[0].message.content
        
        except RateLimitError as e:
            print(f"Rate limit hit (attempt {attempt+1}/{retries}): {e}")
            time.sleep(2 ** attempt)  # exponential backoff

        except OpenAIError as e:
            print(f"OpenAI API error (likely quota issue): {e}")
            break

        except Exception as e:
            print(f"Unhandled error: {e}")
            break

    return "⚠️ Error fetching video content. Please check your API quota or try again later."


