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
import streamlit as st
import plotly.express as px
from ChatClient import ChatClient
from css import css

def run():
    st.set_page_config(
        page_title="Credit Owl",
        page_icon="🦉",
    )

    st.logo(image="./static/images/FLICredit_logo0.png", size="large", icon_image="./static/images/FLICredit_logo1.png")

    #st.markdown(css,unsafe_allow_html=True)
    st.html(css)

    st.write("# Welcome to FLI-Credit! 🦉")

    st.sidebar.success("Select a learning module above.")

    colors = ['#ff9999', '#66b3ff']
    
    figure = px.pie(names=["College students with credit card debt", "College students without credit card debt"], values=[64.8, 35.2], color=colors, hover_name=["College students with credit card debt", "College students without credit card debt"], title="College Students and Credit Card Debt")
    figure2 = px.pie(names=["Low-income college students with credit cards", "Low-income college students without credit cards"], values=[32, 68], color=colors, hover_name=["Low-income college students with credit cards", "Low-income college students without credit cards"], title="Low-Income Students and Credit Cards") ##ARe these values right?

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
    st.plotly_chart(figure, ) ##Update position in doc
    st.divider()
    st.plotly_chart(figure2) ##Update position in doc
    st.divider()

    st.write(
      f"""
      ##### Sources: 
      [What’s the average college student credit card debt? , National Debt Relief](https://www.nationaldebtrelief.com/blog/debt-guide/student-loan-debt/whats-the-average-college-student-credit-card-debt/#:~:text=A%20recent%20study%20by%20College,the%20most%20worry%20and%20concern)
      
      [What every college student needs to know about getting a first credit card, CNBC](https://www.cnbc.com/2024/10/01/what-every-college-student-needs-to-know-about-getting-a-credit-card.html#:~:text=According%20to%20student%20loan%20provider,and%20impart%20valuable%20financial%20lessons)

      [College Student Credit Card Statistics, WalletHub](https://wallethub.com/edu/cc/credit-card-statistics-for-college-students/25535)

      [College Student Debt Statistics, CollegeFinance](https://collegefinance.com/research/college-student-debt-and-credit-card-usage)

      """
  )
    
run()