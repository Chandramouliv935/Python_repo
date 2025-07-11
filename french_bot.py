import re
import random

responses = [
    (r'^(hi|hello|hey)$', [
        "Bonjour ! 👋 (That means 'Hello' in French!)",
        "Salut ! 👋 Try saying it: 'Sah-loo'",
        "Coucou ! That’s a casual hello in French 😊"
    ]),
    (r'^(how are you|how r u|what\'s up)$', [
        "Comment ça va ? (How's it going?)",
        "Ça va bien, et toi ? (I'm good, and you?)",
        "Je vais bien, merci ! Et toi ? 😊"
    ]),
    (r'^(bye|exit)$', [
        "Au revoir ! (Goodbye!) 👋",
        "À bientôt ! (See you soon!) 🇫🇷",
        "Bonne journée ! (Have a nice day!)"
    ]),
    (r'^thank you$', [
        "Merci ! 😊 (That's 'Thank you' in French!)",
        "Merci beaucoup ! (Thank you very much!)",
        "De rien ! (You're welcome!)"
    ]),
    (r'^what is your name$', [
        "Je m'appelle Botinou ! (My name is Botinou!)",
        "On m'appelle Professeur Français 🤓",
        "Moi ? Je suis ton assistant de français !"
    ]),
    (r'.*', [
        "Hmm... I didn't catch that. Try a greeting or a question like 'How are you?'",
        "Want to try saying 'Bonjour' or ask me 'What's your name?' 😊",
        "I'm here to help you learn French! Try typing something simple."
    ])
]

def chatbot():
    print("🇫🇷 French Tutor Bot: Bonjour ! I'm Botinou, your French learning buddy. Type 'bye' or 'exit' to leave.")
    while True:
        user_input = input("You: ").lower().strip()
        for pattern, response_list in responses:
            if re.fullmatch(pattern, user_input):
                response = random.choice(response_list)
                print("Botinou:", response)
                if user_input in ['bye', 'exit']:
                    return
                break

# Run the chatbot
if __name__ == "__main__":
    chatbot()
