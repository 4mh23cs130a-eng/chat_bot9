import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "gpt-4o-mini"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def chat():
    """Interactive chat function"""
    print("=" * 50)
    print("🤖 AI Chat Bot - Powered by DeepSeek")
    print("=" * 50)
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    conversation_history = [
        SystemMessage("You are a helpful assistant.")
    ]
    
    while True:
        # Get user input
        user_input = input("\n👤 You: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("\n👋 Goodbye! Have a great day!")
            break
        
        # Skip empty inputs
        if not user_input:
            print("Please enter a message.")
            continue
        
        # Add user message to history
        conversation_history.append(UserMessage(user_input))
        
        try:
            # Get AI response
            response = client.complete(
                messages=conversation_history,
                temperature=1.0,
                top_p=1.0,
                max_tokens=1000,
                model=model
            )
            
            # Extract and display the response
            ai_response = response.choices[0].message.content
            print(f"\n🤖 AI: {ai_response}")
            
            # Add AI response to history for context
            conversation_history.append(SystemMessage(ai_response))
            
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    chat()