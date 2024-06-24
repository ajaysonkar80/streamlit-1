import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env file (assuming it's in the same directory)
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def chat(prompt):
  """
  Sends a prompt to the Gemini API and returns the response.
  """
  try:
    # Send the prompt and return the generated text
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
  except Exception as e:
    return f"Error: {e}"


# Define page functions
def demo1():
  st.header("Demo 1 - Chat with Gemini")

  # Text input for user prompt
  user_prompt = st.text_input("Enter your message:")

  # Send message to Gemini and display response
  if user_prompt:
    response = chat(user_prompt)
    st.write(f"**Gemini:** {response}")

def demo2():
  st.header("Demo 2")
  st.write("This is the content of Demo 2.")  # Replace with your actual content

def demo3():
  st.header("Demo 3")
  st.write("This is the content of Demo 3.")  # Replace with your actual content


# Streamlit app layout
st.title("Your Streamlit App")

# Create sidebar navigation
st.sidebar.header("Navigation")
page_names = ["Demo 1", "Demo 2", "Demo 3"]
selected_page = st.sidebar.selectbox("Select a Demo", page_names)

# Display selected page content
if selected_page == "Demo 1":
  demo1()
elif selected_page == "Demo 2":
  demo2()
elif selected_page == "Demo 3":
  demo3()
