import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to help you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay", "No problem",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon! :)", "It was nice talking to you. Bye!",]
    ],
]

chatbot = Chat(pairs, reflections)

def main():
    print("Hi! I'm ChatBot. How can I assist you today? (type quit to exit)")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
        if user_input.lower() == "quit":
            break

if __name__ == "__main__":
    main()