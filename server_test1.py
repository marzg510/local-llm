from openai import OpenAI

# client = OpenAI(base_url="http://172.17.208.1:1337/v1", api_key="dummy")
client = OpenAI(base_url="http://192.168.0.25:1337/v1", api_key="dummy")

    # model="tinyllama-1.1b",
completion = client.chat.completions.create(
    temperature=0.0,
    model="Fugaku-LLM-13B-instruct-Q3_K_S.gguf",
    messages=[
        {"role:": "system",
         "content": "あなたは親切なアシスタントです。"},
        {"role": "user",
         "content": "プログラミング言語を2つに分類すると、何と何になりますか？"},
    ]
)
print(completion.choices[0].message.content)
