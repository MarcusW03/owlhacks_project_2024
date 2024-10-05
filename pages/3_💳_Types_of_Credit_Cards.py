import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Types of Credit Cards", page_icon="📈")

st.markdown("# Types of Credit Cards")
st.sidebar.header("Types of Credit Cards")

url = "https://www.capitalone.com/credit-cards/secured-mastercard/"
st.write(
    f"""
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
    You probably don’t have a business at the moment, but if in the future you do, there are business credit cards. 
    They are mainly helpful with organizing business expenses as you can keep track on them through this card and
    keep your business and personal expenses separate. They also provide you with benefits like higher credit limits, 
    rewards, and expense tracking tools to help you manage your business expenses.
    
    ### 6. Secured Credit Cards
    This card works similarly to a regular credit card, BUT the main difference is that a secured credit card requires a (one-time) security deposit
    that acts as collateral for the credit card. 
    Secured credit cards are for people who have no credit history or a bad credit history and want to rebuild it. 

    For example, look at [Capital One’s Quicksilver secured card]({url}).
    
    ### 7. Student Credit Cards 
    You may not have a credit history and that’s okay! Many students don’t and credit card companies understand this, 
    which is why they offer student credit cards for those who are just starting out on their credit journey.
    They usually have lower credit limits and fewer rewards compared to other credit cards.
"""
)

st.divider()

st.write(
    f"""
    ##### Sources: 
    [11 Types of Credit Cards, Capital One](https://www.capitalone.com/learn-grow/money-management/types-of-credit-cards/)
    
    [What is a secured credit card and how does it work?, Capital One](https://www.capitalone.com/learn-grow/money-management/how-secured-credit-cards-work/)

    [Credit Cards, Money Instructor](https://www.moneyinstructor.com/creditcards.asp)

    """
)