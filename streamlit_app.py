import streamlit as st
from huggingface_hub import InferenceClient

import requests

API_URL = "https://sm7x76tjtop3ek5q.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Accept" : "application/json",
	"Authorization": "Bearer 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",
	"Content-Type": "application/json"
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()



def format_prompt(message, history):
    prompt = "<s>"
    for user_prompt, bot_response in history:
        prompt += f"[INST] {user_prompt} [/INST]"
        prompt += f" {bot_response}</s> "
    prompt += f"[INST] {message} [/INST]"
    return prompt

def generate(
    prompt, history, temperature=0.9, max_new_tokens=256, top_p=0.95, repetition_penalty=1.0,
):
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=42,
    )

    formatted_prompt = format_prompt(prompt, history)

    #stream = client.text_generation(formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    #output = ""
    output = query({
	"inputs": prompt,
	"parameters": {"temperature":temperature,"max_new_tokens":max_new_tokens, "top_p": top_p, "repetition_penalty":repetition_penalty }})

    #for response in stream:
     #   output += response.token.text
      #  yield output
    return output[0]["generated_text"]

# Streamlit interface setup
st.title("Cyber Jarvis")

prompt = st.text_area("Write your message here", height=200)
history = []

temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, step=0.05, value=0.9)
max_new_tokens = st.slider("Max new tokens", min_value=0, max_value=1048, step=64, value=256)
top_p = st.slider("Top-p (nucleus sampling)", min_value=0.0, max_value=1.0, step=0.05, value=0.90)
repetition_penalty = st.slider("Repetition penalty", min_value=1.0, max_value=2.0, step=0.05, value=1.2)

output = ""
if st.button("Send"):
   # for response in generate(prompt, history, temperature, max_new_tokens, top_p, repetition_penalty):
    output = generate(prompt, history, temperature, max_new_tokens, top_p, repetition_penalty)
    st.write(output)
