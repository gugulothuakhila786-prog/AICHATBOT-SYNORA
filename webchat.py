import streamlit as st
from ollama import chat

st.title("My AI Chatbot:")
# messages = []
system_message = "You are a shakespearean tutor. Answer in a sentence of 50 words max."
# messages.append({
    
#         "role":"system",
#         "content":system_message 
    
# })
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"user",
            "content":system_message
        } 
        ]
    #  Display previous messages
    for message in st.session_state.messages:
        # Dont display system message
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.write(message["content"])

question = st.chat_input("Ask something...")
if question:
    with st.chat_message("user"):
        st.write(question)
    st.session_state.messages.append({
        "role":"user",
        "content":question
    })

    with st.spinner("uccha aaguthaledha..."):
        response = chat(model= "gemma3:1b", messages=
        st.session_state.messages)
        answer = response.message.content
        with st.chat_message("assistant"):
            st.write(answer)
        st.session_state.messages.append(
            {
                "role":"assisent",
                "content":answer
            }
        )      
