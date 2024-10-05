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
import inspect
import textwrap
import time
import numpy as np
from css import css
# from utils import show_code


def plotting_demo():
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


st.set_page_config(page_title="Why Get A Credit Card?", page_icon="💳")
st.markdown(css,unsafe_allow_html=True)
st.markdown("# Why Get A Credit Card?")
st.sidebar.header("Why Get A Credit Card?")

url = "https://www.annualcreditreport.com/index.action"

st.write(
    f"""
    ##### To answer this question, we first have to explain what a **credit history** is.

    The number of credit cards you have? Do you pay your credit card statements on time? 
    Have you taken out any loans? All of the answers to these questions are included on 
    your credit history. 
    
    This information is collected so that when you apply for loans 
    or a new credit card, businesses can make the decision if they want to let you take 
    out that loan or credit card (so you should pay your credit card on time!). And you 
    won’t have a credit  history if you’ve never had a credit card before or haven’t 
    gotten a loan. 

    Your credit score is a number ranges from 300 to 850, with the 300s being “bad” credit and 800s being “excellent” credit. 

    ##### FUN FACT: 
    By law, you can get a free credit report from each credit bureau from [AnnualCreditReport.com]({url})

    ##### Having a good credit history and score can help out in a variety of ways: 
    - You could get lower interest rates on loans (like mortgages and auto loans) 
    - You could increase your chances of being accepted for a loan 
    - You could be more eligible for better credit card rewards (like higher cash back rewards)
    """
)

st.divider()

st.markdown("### Sample Quiz")

# Question 1
st.write("##### What is the credit score range?")
options1 = ["Select an answer", "300-800", "300-850", "200-800", "400-600"]
answer1 = st.radio("Choose an option:", options1)

if answer1 == "300-850":
    st.success("Correct!")
elif answer1 != "Select an answer":
    st.error("Incorrect. The correct answer is 300-850.")

# Question 2
st.write("##### What does a credit history NOT include?")
options2 = ["Select an answer", "How many credit cards you have", "How often / when you have paid (your credit card)", "Personal income", "Loan history"]
answer2 = st.radio("Choose an option:", options2, key="q2")

if answer2 == "Personal income":
    st.success("Correct!")
elif answer2 != "Select an answer":
    st.error("Incorrect. The correct answer is Personal income.")

st.divider()

st.write(
    f"""
    ##### Sources: 
    [What Is a Credit History? Impact on Scores and Credit Report, Investopedia](https://www.investopedia.com/terms/c/credit-history.asp)
    
    [Your Credit History, Consumer.gov](https://consumer.gov/credit-loans-debt/your-credit-history)

    [6 Reasons You Want a Good Credit Score, Experian](https://www.experian.com/blogs/ask-experian/why-would-you-want-a-good-credit-score/)

    """
)

# plotting_demo()

# show_code(plotting_demo)

