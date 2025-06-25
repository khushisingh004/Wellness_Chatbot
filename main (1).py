print("👋 Welcome to your Virtual Wellness Chatbot 💬")
print("I'm here to support your emotional well-being.")
print("👩‍💻 Created with care by Khushi\n")


def ask_question(question, yes_response, no_response):
           answer = input(question + " (yes/no): ").strip().lower()
           if answer == "yes":
                      print(yes_response)
           elif answer == "no":
                      print(no_response)
           else:
                      print("Please respond with 'yes' or 'no'.")
                      ask_question(question, yes_response, no_response)


print("I'm here to check in on your wellness. Let's begin.\n")

ask_question("1. Would you like to do a quick mood check-in?",
             "Great! On a scale of 1–10, how are you feeling today?",
             "No worries! Let's keep going.")

ask_question("2. Do you feel mentally tired lately?",
             "That's okay. You're not alone in this.",
             "That's wonderful. Stay balanced!")

ask_question("3. Are you sleeping well?",
             "Good sleep is a superpower. Keep it up!",
             "Maybe try a relaxing routine at night.")

ask_question("4. Do you feel stressed today?",
             "Breathe. Try to name your stress—it can help.",
             "That's great to hear!")

ask_question("5. Would you like to try a breathing exercise?",
             "Inhale… hold… exhale… Repeat as needed. 🌬️",
             "Okay. It's always here if you change your mind.")

ask_question("6. Do you want a positive affirmation?",
             "You are doing your best. And that is enough. 💖",
             "No worries. Just remember, you matter.")

ask_question("7. Have you eaten today?",
             "Nice! Eating helps fuel both your body and mind.",
             "Try to eat something small and healthy.")

ask_question("8. Have you done anything fun recently?",
             "That’s great! Joy is healing.",
             "Maybe try something small today, like a favorite song.")

ask_question("9. Are you talking to your friends or family often?",
             "That connection is so valuable.",
             "Try a quick hello to someone you care about.")

ask_question("10. Would you like a self-care tip?",
             "Here's one: Write down 3 things you're grateful for.",
             "No problem! You know yourself best. 💫")

print(
    "\n✨ Thanks for chatting with me. You are strong, and you are not alone. 🌸"
)
print("\nThank you for taking the time to reflect today 💙")
print("Remember, your feelings are valid and you are not alone.")
print("👩‍💻 Stay kind to yourself!")

