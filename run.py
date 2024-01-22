import os
import openai
import gradio as gr

openai.api_key = os.environ['API_KEY']

def predict(message, history):

    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages= history_openai_format,
        temperature=1.0,
        stream=True
    )

    partial_message = ""
    for chunk in response:
        if len(chunk['choices'][0]['delta']) != 0:
            partial_message = partial_message + chunk['choices'][0]['delta']['content']
            yield partial_message

gr.ChatInterface(predict,
                title="Hi! im a Chatbot!",
                description="Ask me anything the Information you want!",
                theme="soft",
                examples=["Who is Nj?", "What is Crptocurrency", "Write program for palindrome in Python"],
                cache_examples=True
                ).launch(share=True)