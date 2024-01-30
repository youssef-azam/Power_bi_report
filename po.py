import streamlit as st

# Set page configuration
st.set_page_config(page_title="Your App", page_icon=":rocket:", layout="wide")

# Define the Power BI dashboard URLs
custom_dimensions_dashboard_url = "https://app.powerbi.com/reportEmbed?reportId=f4fd2081-2550-4ea1-81cf-ccba67fc9472&autoAuth=true&ctid=d1aad15a-5724-45cd-a320-5e75718fa6bd"
default_dimensions_dashboard_url = "https://app.powerbi.com/reportEmbed?reportId=99659cea-34c7-4510-90ef-1dad67d0dc6a&autoAuth=true&ctid=d1aad15a-5724-45cd-a320-5e75718fa6bd"

# Set custom height and width for the first dashboard
custom_width = 1140
custom_height = 541.25
custom_dimensions_html_code = f'<iframe width="{custom_width}" height="{custom_height}" src="{custom_dimensions_dashboard_url}"></iframe>'

# Use Streamlit to display the first Power BI dashboard with custom dimensions
st.markdown(custom_dimensions_html_code, unsafe_allow_html=True)

# Use Streamlit to display the second Power BI dashboard with default dimensions
st.markdown(f'<iframe src="{default_dimensions_dashboard_url}"></iframe>', unsafe_allow_html=True)

# Additional Streamlit app code can be added here

# Run the Streamlit app
if __name__ == "__main__":
    st.write('Hello in my report Powered by Eng: Youssef Azam 👨‍💻, for Manager Eng: Salem 🚀')
