from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

print("AI Agent Ready 🤖 (type 'exit' to stop)")

while True:
    user = input("Tum: ")
    
    if user.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user}]
    )

    print("AI:", response.choices[0].message.content)
