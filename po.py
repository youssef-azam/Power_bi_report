import streamlit as st

# Set page configuration
st.set_page_config(page_title="Your App", page_icon=":rocket:", layout="wide")

# Define the Power BI dashboard URL
power_bi_dashboard_url = "https://app.powerbi.com/reportEmbed?reportId=f4fd2081-2550-4ea1-81cf-ccba67fc9472&autoAuth=true&ctid=d1aad15a-5724-45cd-a320-5e75718fa6bd"

# Use Streamlit to display the Power BI dashboard using Markdown and HTML
st.markdown(f'<iframe width="1200" height="800" src="{power_bi_dashboard_url}"></iframe>', unsafe_allow_html=True)

# Additional Streamlit app code can be added here

# Run the Streamlit app
if __name__ == "__main__":
    
