from ai import get_ai_response

print("Welcome to the AI Chat Bot!")
print("Type 'exit' or 'quit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = get_ai_response(user_input)
    print("AI:", response)