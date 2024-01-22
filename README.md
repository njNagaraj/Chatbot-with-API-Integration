#Chatbot using OpenAi API and gradio

Here i'm using OpenAi api key 

openai.api_key = "API_KEY"
replace the "API_KEY" with your actual API key

Then run pip install -r requirements.txt

Then run python run.py

Experience your chatbot integration on the local server

if you don't know what is gradio head over to https://www.gradio.app/guides/quickstart

Gradio is an open-source Python package that allows you to quickly build a demo or web application for your machine learning model, API, or any arbitary Python function

if you want to change the examples parameter in gr.ChatInterface invoking(Function calling) then delete the 'gradio_cashed_examples' directory and change according to your input examples.
