import streamlit as st
from css import css

def run():
    st.set_page_config(page_title="Using A Credit Card", page_icon="📈")
    st.logo(image="./static/images/FLICredit_logo0.png", size="large", icon_image="./static/images/FLICredit_logo1.png")
    st.markdown(css,unsafe_allow_html=True)
    st.markdown("# Using A Credit Card")
    st.write(
        """
        The moment you’ve been waiting for… HOW SHOULD I USE MY CREDIT CARD? 

        Everyone’s credit card journey is unique, but we’ve grouped some credit card advice here to help you out!

        #### General rule: try not to spend more than you can afford
        This is easier said than done as we understand that we cannot predict what our finances will look like 
        in the future. But trying to be mindful of how much you’re spending with your credit card is an important 
        part of keeping track of your finances! 

        That being said...
        - **Before opening that account, analyze it.** There are so many credit cards out there and they all have 
        their own benefits (and let’s be honest, downsides). With our credit card basics, hopefully you feel 
        equipped to tackle those lengthy card descriptions-because it’s important! Especially keep in mind their interest rates! 
        - **Try to make your payments on time.** This is especially important so that you aren’t running into late fees. 
            - Fun fact: many companies have “autopay” which schedules your payments for you!
        - **Don’t fixate on your credit score.** We have discussed how a credit score can help you get a car loan or mortgage, 
        but this also doesn’t mean that you should check your credit score every hour. 
        And just remember that your credit score CAN CHANGE. 
        - **Keeping old credit card accounts.** Did you know that keeping your old credit card accounts can help your credit 
        score? That is why it is especially important for you to open one at the earliest point that you are able to! 
        """
    )

    st.divider()

    st.write(
        f"""
        ##### Sources: 
        [How To Use A Credit Card: Best Practices Explained, Forbes Advisor](https://www.forbes.com/advisor/credit-cards/how-to-use-a-credit-card/)
        
        [How to Use a Credit Card: Best Practices Explained?, LendingTree](https://www.cnbc.com/select/whats-the-minimum-age-to-be-an-authorized-user-on-a-credit-card/)
        """
    )
run()