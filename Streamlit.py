"""
Streamlit Tutorial - Complete with Code Examples and Expected Outputs

Following the course material by Wahid Hamdi
"""

import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

def main():
    st.title("Streamlit Tutorial")
    st.write("""
    ## What is Streamlit?
    Streamlit is an open-source Python library that makes it easy to create and share 
    beautiful custom web apps for machine learning and data science.
    """)

    # Section 1: Installation and Basic Example
    st.write("""
    ### Installation and Basic Example
    ```python
    pip install streamlit
    
    # Create main.py with:
    import streamlit as st
    st.write('Hello World')
    
    # Run with:
    streamlit run main.py
    ```
    """)
    
    st.write("Hello World")
    st.write("---")

    # Section 2: Input Elements
    st.write("""
    ### Using Input Elements
    Streamlit provides various interactive elements:
    ```python
    # Text input
    x = st.text_input('Favorite Movie?')
    st.write(f"Your favorite movie is: {x}")
    
    # Button
    is_clicked = st.button("Click Me")
    ```
    """)
    
    x = st.text_input('Favorite Movie?')
    st.write(f"Your favorite movie is: {x}")
    
    if st.button("Click Me"):
        st.write("Button was clicked!")
    st.write("---")

    # Section 3: Markdown Formatting
    st.write("""
    ### Markdown Formatting
    ```python
    st.write("## This is a H2 Title!")
    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')
    ```
    """)
    
    st.write("## This is a H2 Title!")
    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')
    st.write("---")

    # Section 4: Working with Data
    st.write("""
    ### Working with Data
    ```python
    # Display data tables
    data = pd.read_csv("movies.csv")
    st.write(data)
    
    # Display charts
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
    st.line_chart(chart_data)
    ```
    """)
    
    # Generate sample data if movies.csv doesn't exist
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"]
    )
    st.bar_chart(chart_data)
    st.line_chart(chart_data)
    st.write("---")

    # Section 5: Multipage Apps
    st.write("""
    ### Multipage Apps
    Create a directory structure:
    ```
    project/
    ├── main.py
    └── pages/
        ├── 1_profile.py
        └── 2_dashboard.py
    ```
    Streamlit automatically organizes pages based on this structure.
    """)
    st.write("---")

    # Section 6: Loan Repayments Calculator
    st.write("""
    ### Loan Repayments Calculator
    Complete example with input fields, calculations, and visualizations:
    """)
    
    st.title("Mortgage Repayments Calculator")
    st.write("### Input Data")
    
    col1, col2 = st.columns(2)
    home_value = col1.number_input("Home Value", min_value=0, value=500000)
    deposit = col1.number_input("Deposit", min_value=0, value=100000)
    interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
    loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)

    # Calculations
    loan_amount = home_value - deposit
    monthly_interest_rate = (interest_rate / 100) / 12
    number_of_payments = loan_term * 12
    monthly_payment = (
        loan_amount
        * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
        / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    )

    # Display results
    total_payments = monthly_payment * number_of_payments
    total_interest = total_payments - loan_amount

    st.write("### Repayments")
    col1, col2, col3 = st.columns(3)
    col1.metric("Monthly Repayments", f"${monthly_payment:,.2f}")
    col2.metric("Total Repayments", f"${total_payments:,.0f}")
    col3.metric("Total Interest", f"${total_interest:,.0f}")

    # Payment schedule
    schedule = []
    remaining_balance = loan_amount

    for i in range(1, number_of_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        year = math.ceil(i / 12)
        schedule.append([
            i, monthly_payment, principal_payment, 
            interest_payment, remaining_balance, year
        ])

    df = pd.DataFrame(
        schedule,
        columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
    )

    st.write("### Payment Schedule")
    payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
    st.line_chart(payments_df)
    st.write("---")

    # Section 7: Deployment
    st.write("""
    ### Deploying to Streamlit Cloud
    1. Publish your app to GitHub
    2. Create requirements.txt:
    ```bash
    pip freeze > requirements.txt
    ```
    3. Click "Deploy" in Streamlit's menu
    4. Select "Streamlit Community Cloud"
    """)

if __name__ == "__main__":
    main()