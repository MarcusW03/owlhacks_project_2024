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
import streamlit as st
# import matplotlib.pyplot as plt

from api_key import my_api_key
from ChatClient import ChatClient
from css import css

LOGGER = get_logger(__name__)

pg = st.navigation([
  #st.Page("app_pages/Home.py", title="Home", icon=":material/add_circle:"), 
  st.Page("app_pages/Why_Get_A_Credit_Card.py", title="Why Get A Credit Card", icon=":material/add_circle:"), 
  st.Page("app_pages/Credit_Card_Terminology.py", title="Credit Card Terminology", icon=":material/add_circle:"), 
  st.Page("app_pages/Types_of_Credit_Cards.py", title="Types of Credit Cards", icon=":material/add_circle:"), 
  st.Page("app_pages/Authorized_User.py", title="Authorized User", icon=":material/add_circle:"), 
  st.Page("app_pages/Using_A_Credit_Card.py", title="Using A Credit Card", icon=":material/add_circle:"), 
  st.Page("app_pages/Analyzing_Some_Credit_Cards.py", title="Analyzing a Credit Card", icon=":material/add_circle:"), 
  st.Page("app_pages/Get_Additional_Information.py", title="Get Additional Information", icon=":material/add_circle:"), 

])



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

    # # Data for the pie chart
    # labels = ['Low-income college students with credit cards', 'College students with credit card debt']
    # sizes = [32, 65]
    # colors = ['#ff9999', '#66b3ff']
    # explode = (0.1, 0)  # explode the 1st slice

    # # Create the pie chart
    # fig1, ax1 = plt.subplots()
    # ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
    #         shadow=True, startangle=90)

    # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # # Display the pie chart in Streamlit
    # st.pyplot(fig1)

    # st.pyplot(fig1)

    st.markdown(
      """
      Finances are tricky for everyone. As a team of current first-generation low-income college seniors, 
      we understand this. It’s very daunting being the first in your family to try to build generational 
      wealth all while having a midterm on Monday. And don’t get me started on the google search rabbit holes… 

      To tackle this issue, **we want you to know you’re not alone.** You can set yourself up for financial success 
      in high school by learning about credit cards and maybe even opening one. Credit cards should not be 
      scary. They can come with many benefits if used **responsibly** and we hope that this website can empower 
      you to see credit cards in a different light. 
      
      **👈 Select a module from the sidebar** to start learning about
      the world of credit!
      """
    )
    st.divider()

    st.write(
      f"""
      ##### Sources: 
      [What’s the average college student credit card debt? , National Debt Relief](https://www.nationaldebtrelief.com/blog/debt-guide/student-loan-debt/whats-the-average-college-student-credit-card-debt/#:~:text=A%20recent%20study%20by%20College,the%20most%20worry%20and%20concern)
      
      [What every college student needs to know about getting a first credit card, CNBC](https://www.cnbc.com/2024/10/01/what-every-college-student-needs-to-know-about-getting-a-credit-card.html#:~:text=According%20to%20student%20loan%20provider,and%20impart%20valuable%20financial%20lessons)

      [College Student Credit Card Statistics, WalletHub](https://wallethub.com/edu/cc/credit-card-statistics-for-college-students/25535)

      """
  )

if __name__ == "__main__":
    pg.run()

    ##use st.snow for celebration?? or st.balloons
