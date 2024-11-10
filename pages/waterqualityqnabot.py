import streamlit as st
import openai 
from openai import OpenAI
import pandas as pd
import os

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI() 

st.title("Water Quality Q&A Bot :material/robot_2:")
st.divider()
option = st.selectbox(
    "Important Key Terms to Know",
    ("pH", "Dissolved Oxygen", "Turbidity", "Nitrate", "Phosphate"),
)
if option == "pH":
    st.write("pH measures how acidic or basic the water is on a scale of 0 to 14.")
if option == "Dissolved Oxygen":
    st.write("Dissolved oxygen refers to the amount of oxygen gas present in water.")
if option == "Turbidity":
    st.write("Turbidity is the cloudiness or haziness of water.")
if option == "Nitrate":
    st.write("Nitrate is a compound found in fertilizers, sewage, and natural mineral deposits")
if option == "Phosphate":
    st.write("Phosphate is another compound found in fertilizers, detergents, and natural deposits.")
prompt = st.text_input("Enter any questions about water quality and I will answer your questions with detailed explanations.")
 
def get_completion(prompt, model="gpt-3.5-turbo"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "system", "content": "You are a professional water quality expert and you will provide detailed explanations and answers to the given prompts. Make sure your explanations and answers are able to be understood by the avergae user."}, 
        {"role": "user", "content": prompt},
        ]
    )
    return completion.choices[0].message.content

with st.form(key = "chat"):    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(get_completion(prompt)) 
        
        


 
        





