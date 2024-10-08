import streamlit as st
import plotly.express as px

st.title("Distribution of Phone and internet states in a pie chart")


df = st.session_state["df"]
color_map_phone = st.session_state["color_map_phone"]
color_map_internet = st.session_state["color_map_internet"] 



feature_counts = df[['State of phone network - bad', 'State of phone network - acceptable', 'State of phone network - good']].sum().reset_index()
feature_counts.columns = ['Feature', 'Count']

# Pie chart showing the frequency of each feature


# Pie chart showing the frequency of each feature with custom colors
fig = px.pie(feature_counts, values='Count', names='Feature', title='State of phone network', color_discrete_map=color_map_phone, color = 'Feature')


st.title('State of phone network')
st.plotly_chart(fig, use_container_width=True)


feature_counts = df[['Status of internet availability - not available', 'Status of internet availability - partially available ', 'Status of internet availability - available']].sum().reset_index()
feature_counts.columns = ['Feature', 'Count']



# Bar chart showing the frequency of each feature
#fig = px.bar(feature_counts, x='Feature', y='Count', title='Status of Internet Availbilty')
fig = px.pie(feature_counts, values='Count', names='Feature', title='Frequency of Status of Internet Availbilty', color_discrete_map=color_map_internet, color = 'Feature')


st.title('Status of Internet')
st.plotly_chart(fig, use_container_width=True)