# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

from api_key import my_api_key
from ChatClient import ChatClient
from css import css

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Credit Owl",
        page_icon="🦉",
    )
    st.markdown(css,unsafe_allow_html=True)

    st.write("# Welcome to Credit Owl! 🦉")

    st.sidebar.success("Select a learning module above.")

    if "client" not in st.session_state:
      chat_client = ChatClient(my_api_key())
      st.session_state.client = chat_client
    else:
      chat_client = st.session_state.client


    st.markdown(
        """
        Fli-Credit is an online learning platform for financial literacy built specifically for
        high schools.
        
        **👈 Select a module from the sidebar** to start learning about
        the world of credit!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()


    ##use st.snow for celebration?? or st.balloons
