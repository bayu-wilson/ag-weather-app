import streamlit as st

st.write("Hello, World")
x = st.text_input("Favorite movie?")
st.write(f"Your favorite movie is: {x}")
is_clicked = st.button("Click me")
st.write("## Title is here")
st.write("description here")
