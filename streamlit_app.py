
import streamlit as st

st.set_page_config(page_title="Main Page", layout="wide")
st.sidebar.title("Main Page")

st.title("🎈 MSBA325 Assignment 3")
st.write(
    "Salim Dallal - skd16"
)

st.write(
    "This page uses data related to Phone and internet service status in Lebanon from the following link: https://linked.aub.edu.lb/pkgcube/data/7acd25e6714ab1d0445637eb8a221b2d_20240909_231115.csv"
)

#!pip install chart_studio
#!pip install plotly
import pandas as pd
# import plotly as py
# import plotly.figure_factory as ff



# Import data from the provided URL
url = "https://linked.aub.edu.lb/pkgcube/data/7acd25e6714ab1d0445637eb8a221b2d_20240909_231115.csv"

@st.cache_data
def GetData(url):
    df = pd.read_csv(url)
    return df


@st.cache_data
def CleanData(df):
    df = df.drop('dataset', axis=1)
    # remove "http://dbpedia.org/resource/" and remove "http://dbpedia.org/page/" from the refArea column

    df['refArea'] = df['refArea'].str.replace("http://dbpedia.org/resource/", "")
    df['refArea'] = df['refArea'].str.replace("http://dbpedia.org/page/", "")
    df['refArea'] = df['refArea'].str.replace("https://dbpedia.org/resource/", "")
    df['refArea'] = df['refArea'].str.replace("https://dbpedia.org/page/", "")
    
    return df




df = CleanData(GetData(url))

st.write("Check the checkbox below to show the cached and cleaned Data")
# Display the first few rows of the DataFrame
if st.checkbox("Display Data"):
    df


st.session_state["df"] = df


color_map_phone = {
    'State of phone network - bad': 'orangered',
    'State of phone network - acceptable': 'slateblue',
    'State of phone network - good': 'mediumaquamarine'
}

st.session_state["color_map_phone"] = color_map_phone

color_map_internet =   {
     'Status of internet availability - not available': 'orangered',
     'Status of internet availability - partially available ': 'slateblue',
     'Status of internet availability - available': 'mediumaquamarine'
 }

st.session_state["color_map_internet"] = color_map_internet