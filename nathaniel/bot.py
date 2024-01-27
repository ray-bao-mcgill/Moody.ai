import os
from openai import OpenAI

client = OpenAI()

def ai_response(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """Given a journal entry, you pick out all words that resemble emotion and\
                respond with all those words separated as a list with commas. Try to pick out the best\
                overall emotion described within the journal entry and put it first on the list. Also,\
                add a colour associated with the best overall emotion and add it last to the list\
                based on colour psychology. For example, if frustrated add the word red at the end\
                of your response."""
            },
            {
                "role": "user",
                "content": message
            }
        ],
        temperature = 1,
        max_tokens = 500,
        top_p = 1,
        frequency_penalty = 1,
        presence_penalty = 1
    )
    response = response.choices[0].message.content
    return response
