import streamlit as st

def chatbot():

    if "client" in st.session_state:
        chat_client = st.session_state.client
    else:
        st.write("Client not initialized...")
        return

    client = chat_client.get_client()
    ai_model = chat_client.get_model()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
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
    
st.set_page_config(page_title="Chat with AI", page_icon="🤖")
st.markdown("# Chat with AI")
st.sidebar.header("Chat with AI")

chatbot()