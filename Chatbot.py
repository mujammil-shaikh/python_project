import openai

# Replace 'YOUR_GPT3_API_KEY' with your actual GPT-3 API key
openai.api_key = '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'

def gpt3_chatbot(user_input):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the appropriate GPT-3 engine
        prompt=user_input,
        max_tokens=100,  # Adjust the length of the generated response
    )

    return response.choices[0].text.strip()

def run_chatbot():
    print("ChatBot: Hello! I am a GPT-3 chatbot. You can start chatting with me. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye! Have a nice day!")
            break

        response = gpt3_chatbot(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    run_chatbot()
