# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Peter Wysocki")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 4 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "* Sine Wave"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

# Tab 4: Sine Wave
with tabs[3]:
    st.subheader(f"Sine Wave")
    
    # Generate data points from 0 to 2*pi
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    # Create a basic static matplotlib figure
    fig, ax = plt.subplots()
    ax.plot(x, y, color='blue')

    # Add basic labels and grid lines
    ax.set_title("y = sin(x)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)

    # Render the static image of the graph in Streamlit
    st.pyplot(fig)



