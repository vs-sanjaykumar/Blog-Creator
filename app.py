import streamlit as st
import os
import google.generativeai as genai

from apikey import google_gemini_api_key

genai.configure(api_key=google_gemini_api_key)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="Generate a comprehensive engaging blog relevant to the given title and keywords . The blog should be approximately {num_words} words in length , suitable for an online audience . Ensure the content is original , informative and maintains a consostent tone throughout.",
)



st.set_page_config(layout="wide")

# TITLE for app
st.title("BlogCraft : Your AI Writing Companion")

# Subheader
st.subheader("You can create perfect blog with this app")

#sidebar for user input
with st.sidebar:
    st.title("Input your Blog Details")
    st.subheader("Enter the details of blog that you want to generate")

    #Blog Title
    blog_title=st.text_input("Blog Title")

    # Keyword input
    keywords=st.text_area("Keywords (comma-seperated)")

    #Number Of Words
    num_words=st.slider("Number of Words",min_value=100,max_value=2000,step=100)

    #Number of Images
    num_images=st.number_input("NUmber of Images",min_value=1,max_value=5,step=1)


    submit_button=st.button("Generate Blog")

if submit_button:
        
    input_message = (
            f"Generate a comprehensive, engaging blog post relevant to the title: {blog_title}. "
            f"Include the following keywords: {keywords}. The blog should be approximately {num_words} words in length."
        )

        # Start chat and send message
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(input_message)

        # Display the response
    if response:
            st.write(response.text)
    else:
            st.write("No response from the AI.")
