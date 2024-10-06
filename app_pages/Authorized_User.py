import streamlit as st
import time
import numpy as np
from css import css

st.set_page_config(page_title="Authorized User on Credit Cards", page_icon="📈")
st.markdown(css,unsafe_allow_html=True)
st.markdown("# Authorized User on Credit Cards")
st.sidebar.header("Authorized User on Credit Cards")
st.write(
    """
    ##### Being an Authorized User
    Maybe you’re not 18 yet, but you really want to have a credit card account and start building your own credit, 
    you could be added as an authorized user to someone who already has a credit card. The age that you can be an 
    authorized user on someone’s credit card account differs from company to company. To see some examples of 
    the ages for different companies look [here](https://www.cnbc.com/select/whats-the-minimum-age-to-be-an-authorized-user-on-a-credit-card/)!

    As an authorized user, you can make purchases with the credit card owner’s account. **BUT** you should note that the 
    credit history of the person whose account you are an authorized user on will affect your own credit history 
    (this can be both positive or negative depending on the credit card holder’s credit history).

    If the primary cardholder has good credit habits, such as paying on time and keeping balances low, you may benefit from their good credit habits.
    However, if the primary cardholder has poor credit habits, such as paying late or carrying high balances, you may be negatively impacted.

    Being an authorized user on someone else's credit card account can be a good way to build or rebuild credit.

    """
)

st.markdown("### Sample Quiz")

# Question 1
st.write("##### I am authorized user on my dad’s credit card, and he recently missed a credit card payment. Does this affect my credit?")
options1 = ["Select an answer", "True", "False"]
answer1 = st.radio("Choose an option:", options1)

if answer1 == "True":
    st.success("Correct!")
    st.balloons()
elif answer1 != "Select an answer":
    st.error("Incorrect. The correct answer is True.")

# Question 2
st.write("##### Since I’m not 18, I cannot be an authorized user.")
options2 = ["Select an answer", "True", "False"]
answer2 = st.radio("Choose an option:", options2, key="q2")

if answer2 == "False":
    st.success("Correct!")
    st.balloons()
elif answer2 != "Select an answer":
    st.error("Incorrect. The correct answer is False.")

st.divider()

st.write(
    f"""
    ##### Sources: 
    [What Is an Authorized User on a Credit Card?, Equifax](https://www.equifax.com/personal/education/credit-cards/articles/-/learn/authorized-user-on-a-credit-card/#:~:text=An%20authorized%20user%20is%20someone,remains%20with%20the%20primary%20cardholder)
    
    [What’s the minimum age to be an authorized user on a credit card?, CNBC](https://www.cnbc.com/select/whats-the-minimum-age-to-be-an-authorized-user-on-a-credit-card/)

    [Can being an authorized user build your credit?, Chase](https://www.chase.com/personal/credit-cards/education/build-credit/do-authorized-users-on-credit-cards-build-credit#:~:text=Being%20added%20as%20an%20authorized%20user%20on%20another%20person%27s%20card,users%20see%20eye%20to%20eye)

    """
)