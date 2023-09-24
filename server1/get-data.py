import requests
import pandas as pd

# API URLs
first_link = "https://itsnt2259.iowa.uiowa.edu/piwebapi/elements/F1EmAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfgSVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJO/attributes?startIndex=0"
last_link = "https://itsnt2259.iowa.uiowa.edu/piwebapi/elements/F1EmAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfgSVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJO/attributes?startIndex=0"

username = 'iowa\\akislam'
password = 'Qwertrty#1169046'
# Function to fetch data from the API and return as JSON
def fetch_data(url):
    response = requests.get(url,auth=(username,password))
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Failed to fetch data from {url}. Status code: {response.status_code}")

# Fetch data from API
first_data = fetch_data(first_link)
#last_data = fetch_data(last_link)

# Extract items from the JSON response
items = first_data["Items"] #+ last_data["Items"]

# Create a DataFrame from the extracted data
df = pd.json_normalize(items)

# Display the DataFrame
print(df)