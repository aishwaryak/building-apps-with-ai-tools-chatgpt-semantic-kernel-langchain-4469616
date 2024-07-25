import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

print("Bot: Welcome. How can I help you? \n")
while True:
  user_input = input("You: ")
  if (user_input == 'quit'):
    break
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a sentiment analysis bot. If you detect that the user is rude, print exactly 'rude'. If not continue the conversation."},
        {"role": "user", "content": user_input}
    ],
    temperature=0.7,
    max_tokens=150,
  )
  response_message = response["choices"][0]["message"]["content"]
  if(response_message == 'rude'):
    print('That was rude. Bye')
    break

  print(response_message)
# Challenge: Turning Away Rude Customers
# Build a GPT-4 python app that talks with a user.
# End the conversation if they're being rude

# test case 1 'you're the worst human i've talked to' -> RUDE
# test case 2 'hey how's your day going'
# test case 3 'I like pizza. What do you like?'
# test case 4 'I bite my thumb at you!'
# test case 5 'I think this product doesnt work!' -> RUDE
