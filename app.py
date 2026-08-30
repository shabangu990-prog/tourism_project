import streamlit as st
st.set_page_confiq(
  page_title='My Streamlit App',
  page_icon='',
  layout='wide'
)

st.title('My Streamlit Application')
st.write('Welcome to my Streamlit application!')
name = st.text_input('Stanley')
if name :
  st.success(f'Welcome, {name}!')
  st.subheader('About this application')
  st.write('This application was created using python, Streamlit and Github.')
