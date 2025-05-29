import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable.")

genai.configure(api_key=api_key)
def main():
    print("Welcome to the Gemini Multi-Turn Chat Playground!")
    print("Enter your message one by one.")
    print("Type 'done' when finished to receive the final Gemini response.\n")
    temperature = 0.0
    try:
        temperature = float(input("Enter temperature (0.0 to 1.0, default is 0.7): ") or "0.7")
        if temperature <= 0.0 or temperature >= 1.0:
            raise ValueError("Temperature must be between 0.0 and 1.0.")
    except ValueError:
        print("Invalid temperature input. Using default value of 0.7.")
        temperature = 0.7
        
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"temperature": temperature}
    )
    
    chat = model.start_chat(history=[])
    
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'done':
            break
        
        chat.send_message(user_input)
        
    print("Final Gemini Response:")
    response = chat.send_message("Please summarize our conversation.")
    print("--------------------------------------------------")
    
    print(response.text)
    
if __name__ == "__main__":
    main()
