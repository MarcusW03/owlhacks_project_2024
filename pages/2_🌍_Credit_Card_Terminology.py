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
import pandas as pd
import pydeck as pdk
# from utils import show_code


from urllib.error import URLError


def mapping_demo():
    @st.experimental_memo
    def from_data_file(filename):
        url = (
            "http://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename
        )
        return pd.read_json(url)

    try:
        ALL_LAYERS = {
            "Bike Rentals": pdk.Layer(
                "HexagonLayer",
                data=from_data_file("bike_rental_stats.json"),
                get_position=["lon", "lat"],
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
            "Bart Stop Exits": pdk.Layer(
                "ScatterplotLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_color=[200, 30, 0, 160],
                get_radius="[exits]",
                radius_scale=0.05,
            ),
            "Bart Stop Names": pdk.Layer(
                "TextLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_text="name",
                get_color=[0, 0, 0, 200],
                get_size=15,
                get_alignment_baseline="'bottom'",
            ),
            "Outbound Flow": pdk.Layer(
                "ArcLayer",
                data=from_data_file("bart_path_stats.json"),
                get_source_position=["lon", "lat"],
                get_target_position=["lon2", "lat2"],
                get_source_color=[200, 30, 0, 160],
                get_target_color=[200, 30, 0, 160],
                auto_highlight=True,
                width_scale=0.0001,
                get_width="outbound",
                width_min_pixels=3,
                width_max_pixels=30,
            ),
        }
        st.sidebar.markdown("### Map Layers")
        selected_layers = [
            layer
            for layer_name, layer in ALL_LAYERS.items()
            if st.sidebar.checkbox(layer_name, True)
        ]
        if selected_layers:
            st.pydeck_chart(
                pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state={
                        "latitude": 37.76,
                        "longitude": -122.4,
                        "zoom": 11,
                        "pitch": 50,
                    },
                    layers=selected_layers,
                )
            )
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )


st.set_page_config(page_title="Credit Card Terminology", page_icon="🌍")
st.markdown("# Credit Card Terminology")
st.sidebar.header("Credit Card Terminology")
st.write(
    """
    ###### The world of credit cards is filled with jargon that can be confusing. 
    ##### Here are some common terms you should know:

    #### Credit Limit
    A credit limit is the maximum amount of money a lender will allow a borrower to spend using a credit card or revolving line of credit.

     #### Credit Card Balance
    A credit card balance is the amount of money owed on a credit card account.

    #### Credit Utilization
    Credit utilization is the ratio of a borrower's total credit card balances to their total credit card limits.

    #### Credit Card Statement
    A credit card statement is a summary of how you've used your credit card for a billing period.

    #### Credit Card Payment
    A credit card payment is a payment made by a credit card holder toward a credit card account.

     #### Minimum Payment
    The minimum payment is the smallest amount of a credit card bill that a credit card holder must pay each month to keep the account in good standing.

    #### Credit Card Debt
    Credit card debt is a type of unsecured liability that is incurred through revolving credit card loans.
    
    #### Interest Rate
    An interest rate is the amount of interest due per period, as a proportion of the amount lent, deposited, or borrowed.
    Refers to how much the credit card company charges you for borrowing money (and is related to the APR).

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
    The annual percentage rate (APR) on a credit card is the interest rate charged on outstanding credit card balances.

    #### Credit Card Benefits
    Credit card benefits are the perks or advantages that come with using a credit card.

    #### Credit Card Rewards
    Credit card rewards are points, miles, or cash back you earn for making purchases with a credit card.
    """
)

# mapping_demo()

# show_code(mapping_demo)