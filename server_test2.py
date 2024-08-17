from openai import AsyncOpenAI
import chainlit as cl

client = AsyncOpenAI(base_url="http://192.168.0.25:1337/v1", api_key="dummy")

@cl.on_message
async def on_message(input):
  completion = await client.chat.completions.create(
    # temperature=0.0,
    # model="Fugaku-LLM-13B-instruct-Q3_K_S.gguf",
    model="tinyllama-1.1b",
    messages=[
        {"role:": "system",
         "content": "あなたは親切なアシスタントです。"},
        {"role": "user",
         "content": input.content}
    ]
  )
  await cl.Message(content=completion.choices[0].message.content).send()
