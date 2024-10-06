import streamlit as st
from css import css

st.set_page_config(page_title="Analyzing Examples Credit Cards", page_icon="📈")
st.markdown(css,unsafe_allow_html=True)
st.markdown("# Analyzing Examples Credit Cards")
st.sidebar.header("Analyzing Examples Credit Cards")
st.write(
    """
    We understand that this information is a lot (take a deep breath)! So, in addition to the 
    information pages we’ve provided, we also wanted to provide an example of us going through a sample credit card. 

    For this example we will walk through a **fake student credit card**, FLI Credit, as we don’t want any legal issues: 
    """
)

container = st.container(border=True)

container.write(
    """
    #### Welcome to FLI Credit!

    We are happy that you’re considering opening a credit card account with us at FLI Credit! We have all our information outlined 
    here for your convenience:
    
    
    ###### 3% Cash Back 
    Earn 3% on select stores like Store A and Store B! But, you also get 1% cash back on all other purchases.  

    
    Exclusive to our loyal student customers, we offer no annual fees! 

    We make balance transfers easy! We have a fixed APR, 11% for your first 6 months of opening this credit card for balance transfers. After the 6 months, the APR can vary from 12% to 20% depending on your credit score. 

    Need a cash advance? Our APR for cash advances is only 25%! 

    Please try to not miss any payments! For any late payment, we will charge a base fee of $30. 
    """
)

st.divider()

st.markdown("### Sample Quiz")

# Question 1
st.write("##### If I make a purchase from Store C, how much cash back can I get from my purchase?")
options1 = ["Select an answer", "2%", "1%", "3%", "None"]
answer1 = st.radio("Choose an option:", options1)

if answer1 == "1%":
    st.success("Correct!")
    st.balloons()
elif answer1 != "Select an answer":
    st.error("Incorrect. The correct answer is 1%.")

# Question 2
st.write("##### I just opened up the FLI Credit, do I have to make a yearly payment for having this credit card?")
options2 = ["Select an answer", "True", "False"]
answer2 = st.radio("Choose an option:", options2, key="q2")

if answer2 == "False":
    st.success("Correct!")
    st.balloons()
elif answer2 != "Select an answer":
    st.error("Incorrect. The correct answer is False.")

# Question 3
st.write("##### I have had the FLI credit card for 5 months. And I really want to transfer my balance to another credit card, is my APR fixed (11%) or is it a variable APR (12% to 20%)?")
option3 = ["Select an answer", "Fixed APR", "Variable APR"]
answer3 = st.radio("Choose an option:", option3, key="q3")

if answer3 == "Fixed APR":
    st.success("Correct!")
    st.balloons()
elif answer3 != "Select an answer":
    st.error("Incorrect. The correct answer is Fixed APR.")

# Question 4
st.write("##### This is the third time I’ve missed my credit card payment date. How much do I pay (excluding the balance that you owe)?")
options4 = ["Select an answer", "$40", "$25", "$30", "$15"]
answer4 = st.radio("Choose an option:", options4)

if answer4 == "$30":
    st.success("Correct!")
    st.balloons()
elif answer4 != "Select an answer":
    st.error("Incorrect. The correct answer is $30.")