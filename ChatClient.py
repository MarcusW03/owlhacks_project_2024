import streamlit as st
from openai import OpenAI

class ChatClient():

    def __init__(self, api_key, model="gpt-4-turbo", description="openai_model"):
    
        self.client = OpenAI(api_key=api_key)

        self.model = model
        st.session_state[description] = self.model

        st.session_state.messages = []
    
    def get_client(self):
        return self.client
    
    def get_model(self):
        return self.model