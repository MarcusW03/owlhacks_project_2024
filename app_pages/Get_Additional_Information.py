import streamlit as st
from api_key import my_api_key
from ChatClient import ChatClient
from css import css

def chatbot():

    if "client" in st.session_state:
        chat_client = st.session_state.client
    else:
        chat_client = ChatClient(my_api_key())
        st.session_state.client = chat_client

    client = chat_client.get_client()
    ai_model = chat_client.get_model()
    ai_image = './static/images/FLICredit_logo2.png'
    user_image = './static/images/user_image.png'

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        avatar = ai_image if message["role"] == "assistant" else user_image
        
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Need additional information?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user", avatar=user_image):
            st.markdown(prompt)

        try:
            # Display assistant response in chat message container
            with st.chat_message("assistant", avatar=ai_image):
                stream = client.chat.completions.create(
                    model=ai_model,
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
                response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.toast("Whoops, there seems to be an error with the chatbot\n\n" + str(e))
    
st.set_page_config(page_title="AI Help", page_icon="🤖")
st.markdown("# Get Additional Information from AI")
st.markdown("*This content has been created by an AI language model and is intended to provide general information. While we strive to deliver accurate and reliable content, it may not always reflect the latest developments or expert opinions. The content should not be considered as professional or personalized advice. We encourage you to seek professional guidance and verify the information independently before making decisions based on this content.*")
#st.sidebar.header("Chat with AI")
st.markdown(css,unsafe_allow_html=True)

chatbot()