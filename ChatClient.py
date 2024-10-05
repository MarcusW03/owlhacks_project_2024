import streamlit as st
from openai import OpenAI

class ChatClient():

    def __init__(self, api_key):
    
        self.client = OpenAI(api_key=api_key)

        self.model = "gpt-3.5-turbo"
        st.session_state["openai_model"] = self.model

        st.session_state.messages = []
    
    def get_client(self):
        return self.client
    
    def get_model(self):
        return self.model