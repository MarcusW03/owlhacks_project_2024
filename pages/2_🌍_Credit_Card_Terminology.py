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
from css import css

st.set_page_config(page_title="Credit Card Terminology", page_icon="🌍")
st.markdown(css,unsafe_allow_html=True)
st.markdown("# Credit Card Terminology")
st.sidebar.header("Credit Card Terminology")
st.write(
    """
    ###### The world of credit cards is filled with jargon that can be confusing. 
    ##### Here are some common terms you should know:

    """
)

st.write(
    """
    #### Credit Limit
    A credit limit is the maximum amount of money a lender will allow a borrower to spend using a credit card or revolving line of credit.

     #### Credit Card Balance
    A credit card balance is the amount of money owed on a credit card account.

    #### Credit Utilization
    Credit utilization is the ratio of a borrower's total credit card balances to their total credit card limits.

    #### Credit Card Statement
    A credit card statement is a summary of how you've used your credit card for a billing period.
""")

st.divider()

st.write(
    """
    #### Credit Card Payment
    A credit card payment is a payment made by a credit card holder toward a credit card account.

     #### Minimum Payment
    The minimum payment is the smallest amount of a credit card bill that a credit card holder must pay each month to keep the account in good standing.

    #### Credit Card Debt
    Credit card debt is a type of unsecured liability that is incurred through revolving credit card loans.
    
    #### Interest Rate
    An interest rate is the amount of interest due per period, as a proportion of the amount lent, deposited, or borrowed.
    Refers to how much the credit card company charges you for borrowing money (and is related to the APR).
    """)
st.divider()

st.write(
    """
    #### Credit Score
    A credit score is a numerical expression based on a level analysis of a person's credit files, to represent the creditworthiness of an individual.
    Scores range from 300 to 850 with the 300s being “bad” credit and 800s being “excellent” credit.
    
    #### Credit Report
    A credit report is a detailed report of an individual's credit history prepared by a credit bureau.

    #### Credit History
    Credit history is a record of a borrower's responsible repayment of debts including any loans you have/ have had, number of credit cards, and your credit card payment history.

    #### Credit Inquiry
    A credit inquiry is a request by a legitimate business to check the credit history of a potential customer.

    #### Credit Freeze
    A credit freeze is a security measure that restricts access to your credit report.

    #### Credit Card Fraud
    Credit card fraud is a wide-ranging term for theft and fraud committed using or involving a payment card, such as a credit card or debit card, as a fraudulent source of funds in a transaction.

    #### Credit Card APR
    If you borrow money through your credit card, the APR represents the total annual cost of borrowing money as it includes the 
    interest rate of borrowing and any other fees. However, there are two types of APR’s: fixed APR and variable APR, 
    where a fixed APR remains the same while a variable APR is subject to change. 
    """
    )

st.divider()

st.write(
    """
    #### Credit Card Benefits
    Credit card benefits are the perks or advantages that come with using a credit card.

    #### Credit Card Rewards
    Credit card rewards are points, miles, or cash back you earn for making purchases with a credit card.

    #### Balance Transfer
    Refers to when you move some of your credit card debt to another card, (which can be subject to fees!)

    #### Cash Advance
    A cash advance is a service provided by credit card issuers that allows cardholders to withdraw a certain amount of cash. 
    Note that these withdrawals can be subject to high interest rates and other fees!  
    """
)

st.divider()

st.markdown("### Sample Quiz")

# Question 1
st.write("##### What does this definition refer to: **“When you take out money from your credit card**?")
options1 = ["Select an answer", "APR", "Credit Score", "Interest Rate", "Cash Advance"]
answer1 = st.radio("Choose an option:", options1)

if answer1 == "Cash Advance":
    st.success("Correct!")
    st.balloons()
elif answer1 != "Select an answer":
    st.error("Incorrect. The correct answer is Cash Advance.")

# Question 2
st.write("##### What does this definition refer to: **“The maximum credit you can use on your credit card**?")
options2 = ["Select an answer", "Credit Limit", "Credit Score", "Credit History", "Annual Fee"]
answer2 = st.radio("Choose an option:", options2, key="q2")

if answer2 == "Credit Limit":
    st.success("Correct!")
    st.balloons()
elif answer2 != "Select an answer":
    st.error("Incorrect. The correct answer is Credit Limit.")

# Question 3
st.write("##### What does this definition refer to: **“The total annual cost of borrowing money from your card**?")
option3 = ["Select an answer", "APR", "Credit Score", "Interest Rate", "Balance Transfer"]
answer3 = st.radio("Choose an option:", option3, key="q3")

if answer3 == "APR":
    st.success("Correct!")
    st.balloons()
elif answer3 != "Select an answer":
    st.error("Incorrect. The correct answer is APR.")

st.divider()

st.write(
    f"""
    ##### Sources: 
    [Credit Card Key Terms, CFPB](https://www.consumerfinance.gov/consumer-tools/credit-cards/answers/key-terms/)
    
    [Your Credit History, Consumer.gov](https://consumer.gov/credit-loans-debt/your-credit-history)

    [What Is an APR and How Does It Work?, Experian](https://www.experian.com/blogs/ask-experian/what-is-apr/)

    [25 key terms everyone with a credit card should know, CNBC](https://www.cnbc.com/select/common-credit-card-terms/)

    """
)

# mapping_demo()

# show_code(mapping_demo)
