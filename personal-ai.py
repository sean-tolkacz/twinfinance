import openai

# Set your API key
openai.api_key = "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"

# Make a request to the OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-4o-mini",  # Use the correct model name
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)

# Print the response
print(response.choices[0].message['content'])
