import streamlit as st
import openai
openai.api_key = "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"
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "
def openai_create(prompt):
    response = openai.Completion.create(
        model=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text
st.write(openai_create("write a leave letter "))
