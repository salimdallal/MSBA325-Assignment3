import streamlit as st
import plotly.express as px

st.title('Bar Charts')
st.title('State of Phone by Area comparison')

df = st.session_state["df"]
color_map_phone = st.session_state["color_map_phone"]
color_map_internet = st.session_state["color_map_internet"]


# Group by 'refArea' and sum the values for the specified columns
feature_counts = df.groupby('refArea')[['State of phone network - bad', 'State of phone network - acceptable', 'State of phone network - good']].sum().reset_index()

# Transpose the DataFrame to have features as columns
feature_counts = feature_counts.melt(id_vars=['refArea'], var_name='Feature', value_name='Count')

# Bar chart showing the frequency of each feature grouped by 'refArea'
fig = px.bar(feature_counts, x='refArea', y='Count', color='Feature', title='State of phone network by Area', color_discrete_map=color_map_phone)

st.plotly_chart(fig, use_container_width=True)



st.title('Status of Internet by Area comparison')

# Group by 'refArea' and sum the values for the specified columns
feature_counts = df.groupby('refArea')[['Status of internet availability - not available', 'Status of internet availability - partially available ', 'Status of internet availability - available']].sum().reset_index()

# Transpose the DataFrame to have features as columns
feature_counts = feature_counts.melt(id_vars=['refArea'], var_name='Feature', value_name='Count')

# Bar chart showing the frequency of each feature grouped by 'refArea'
fig = px.bar(feature_counts, x='refArea', y='Count', color='Feature', title='Status of Internet Availability by Area', color_discrete_map=color_map_internet)

st.plotly_chart(fig, use_container_width=True)