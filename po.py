import streamlit as st

# Set page configuration
st.set_page_config(page_title="Your App", page_icon=":rocket:", layout="wide")

# Define the Power BI dashboard URL
power_bi_dashboard_url = "https://app.powerbi.com/reportEmbed?reportId=f4fd2081-2550-4ea1-81cf-ccba67fc9472&autoAuth=true&ctid=d1aad15a-5724-45cd-a320-5e75718fa6bd"

# Set custom height and width
custom_width = 1200
custom_height = 800

# Use Streamlit to display the Power BI dashboard using Markdown and HTML with custom height and width
st.markdown(f'<iframe width="{custom_width}" height="{custom_height}" src="{power_bi_dashboard_url}"></iframe>', unsafe_allow_html=True)

# Additional Streamlit app code can be added here

# Run the Streamlit app
if __name__ == "__main__":
  st.write('Hello in my report')
