from openai import OpenAI

client=OpenAI(api_key="your_api_key-here")
user_prompt=input("prompt: ")
system_prompt="Limit your answer to one sentence."

response=client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system" , "content":=system_prompt},
        {"role": "user","content":user_prompt}
        ]
)
print(response.choices[0].message.content)