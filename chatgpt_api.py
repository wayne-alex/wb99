import openai

api_key = 
api_key1 = 
openai.api_key = api_key1

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
        timeout=None,
    )
    return response.choices[0].text.strip()

# Example usage
while True:
    user_input = input("User: ")
    prompt = f'User: {user_input}\nChatGPT: '
    response = generate_response(prompt)
    print("ChatGPT:", response)
