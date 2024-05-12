# Try index.py if you want to try this assignment by Streamlit; otherwise, use this file instead.
from openai import OpenAI
# I didn't want to commit my API key to history (wasn't sure if repo is public or private), so instead I've loaded up dotenv so when you clone this down, you can create a .env file to add your openai key to.
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

chat_logs = []


def generate_response(user_input):
    try:
        comp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Assume the role of a Python teacher by the name of Mr. Green. You think step by step and believe in OOP."},
                      {"role": "user", "content": user_input}]
        )
        chat_logs.append({"user": user_input, "bot": comp.choices[0].message.content})
        return comp.choices[0].message
    except Exception as e:
        print('Error generating response:', e)
        return "I'm sorry, I couldn't generate a response."


def main():
    user_input = input('Python student question: ')
    if user_input.lower() == "quit":
        print("Exiting Python study bot")

    response = generate_response(user_input)
    print('Study bot says: ', response.content, '\n\n\n')
    print('History of logs: ', chat_logs)


if __name__ == "__main__":
    main()