import streamlit as st
import requests

option = st.selectbox(
    "Please select a datasource", ("Local Directory", "Drive", "Web Link")
)

if option == "Web Link":
    with st.form("web_link_form"):
        st.write("Please enter a link to scrape")
        url = st.text_input("URL")
        submit = st.form_submit_button(label="Submit")
        if submit:
            try:
                response = requests.post(
                    url="localhost:8000/web_link", data={"web_link": url}, timeout=5
                )
            except Exception as e:
                raise e
            st.write(response.text)
elif option == "Drive":
    st.write("Please enter a public drive link")
    st.write("Feature coming soon")
else:
    st.write("Please enter a directory path")
    st.write("Feature coming soon")
