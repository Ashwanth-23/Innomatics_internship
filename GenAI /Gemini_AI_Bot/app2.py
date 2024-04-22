import google.generativeai as genai
import streamlit as st

#load the Gemini API key 
f = open(r"C:\Users\ADMIN\Desktop\Data Sicence\innomatics internship\Gen-Application\keys\.gemeniai.txt")
key = f.read()

#configure the api key to genai 
genai.configure(api_key = key)

# Given the Title as the AI Tutor For DataScience  
st.title("AI Tutor For DataScience")

# If there is no chat_history in session, init one 
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

#Init Gemini model
ai = genai.GenerativeModel(model_name = "gemini-1.5-pro-latest",
                           system_instruction = "you are AI Assistant to reslove the Queries of the user related to Data Science.")


#Init the chat object 
chat = ai.start_chat(history=st.session_state["chat_history"])

# Iterate over chat history and diaplay message 
for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text,key= msg.role)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message (user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"] = chat.history
    