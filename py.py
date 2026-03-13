import streamlit as st

# Set the title of the app
st.title("Interactive Streamlit App")

# Taking user input
# Corrected 'maest.test_input' to 'st.text_input'
name = st.text_input("Enter your name:")

# Displaying a message when a button is clicked
if st.button("Submit"):
    # Using an f-string to properly inject the 'name' variable
    st.write(f"Hello, {name}! Welcome to Streamlit.")
