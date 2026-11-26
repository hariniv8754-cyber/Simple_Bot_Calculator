print("Welcome to the Chatbot!")
conversation = []
Reply = {
    "Hello": "Hi there! How can I assist you today?",
    "How are you?": "I'm just a bot, but I'm functioning as expected!",
    "What can you do?": "I can perform calculations, provide information, and assist with various tasks.",
    "What is your name?": "I am Simple Bot, your friendly assistant.",
}
while True:
    user = input("You: ")
    if user.lower()=="bye":
        print("Bot: Goodbye and have a great day!!")
        break
    conversation.append({"role": "user", "content": user})
    if user in Reply:
        print("Bot:",Reply[user])
    else:
        print("Bot: Sorry , I can't Understand")
        print("Bot: Please retry")