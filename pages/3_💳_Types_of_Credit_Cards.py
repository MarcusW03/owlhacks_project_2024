import streamlit as st
import time
import numpy as np
from css import css

st.set_page_config(page_title="Types of Credit Cards", page_icon="📈")
st.markdown(css,unsafe_allow_html=True)
st.markdown("# Types of Credit Cards")
st.sidebar.header("Types of Credit Cards")
st.write(
    """
    ### Did you know there are 11 kinds of credit cards?
    This may sound overwhelming, but don’t worry! We are here to give you the basics! In this lesson we go over
    the top 7 most common types of credit cards.

    #### 1. Cash back Credit Cards
    When you buy certain things (i.e. groceries), you could get a percentage of your money back. 
    Some cards provide the same percentage for all purchases, but others vary depending on what 
    you buy (i.e. they might give 3% cashback for groceries and 5% for entertainment). 

    ### 2. Points Credit Cards 
    Similar to cash back credit cards, you can earn points for your purchases in specific categories. 
    These points could be redeemed in different forms, like cash back and gift cards.

    ### 3. Travel Rewards credit cards
    Do you travel a lot? (Or maybe you plan to!) You may want to consider a travel rewards credit card 
    as they reward you with “miles” for your purchases. Miles can be used to help you buy a flight 
    or in some cases book a hotel room. Some cards even offer other travel benefits. 

    ### 4. Store credit cards 
    Have you ever been to GAP or Best Buy and have been asked: “would you like to open up a card with us”? 
    These are store credit cards, which can be helpful if you frequent the specific store often as 
    they may provide specific discounts exclusive to card holders, like 5% back on every purchase. 
    And be careful! Sometimes the store credit card can only be used at that specific store. 

    ### 5. Business Credit Cards
    Business credit cards are for small business owners. They can help you keep your business and personal expenses separate.
    They also provide you with benefits like higher credit limits, rewards, and expense
    tracking tools to help you manage your business expenses.
    
    ### 6. Secured Credit Cards
    Secured credit cards are for people who have no credit history or a bad credit history. 
    They require a security deposit that acts as collateral for the credit card.
    The credit limit is usually equal to the amount of the security deposit.
    Secured credit cards can help you build or rebuild your credit history.
    
    ### 7. Student Credit Cards 
    Student credit cards are for college students who have little to no credit history.
    They usually have lower credit limits and fewer rewards compared to other credit cards.
    Student credit cards can help you build your credit history while you're in school.

"""
)