from openai import OpenAI
import streamlit as st

#read the API key and setup an openai client 
f = open(r"C:\Users\ADMIN\Desktop\Data Sicence\innomatics internship\Gen-Application\keys\.openai.txt")
key = f.read()
client = OpenAI(api_key=key)

##############################
st.snow()
st.title("PYTHON CODE DEBUGGER")
st.subheader("Review your code")
###############################

#Take user's input 
prompt = st.text_area("Enter your python code")
# If the button is clicked, generate reponses
if st.button("Generate") == True:
    #st.balloons()
    response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = [
                    {"role":"system", "content" : """ you are  a helpful AI Assistant as a python code 
                      debugger, you will a  python code as input from user, you job is explain the bugs 
                     and fix the bug. and generate the correct one as output.
                     generate the output as  below format 
                     bugs : "errors of code", and explain the bugs and review , Fixed code : "correct code"
                                                          
                                                  """},
                    {"role": "user", "content" : prompt}
                ], temperature = 0.7
    )
    #print the reponse on the web app 
    st.write(response.choices[0].message.content)
