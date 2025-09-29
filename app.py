import streamlit as st
import google.generativeai as genai
import os

# Configure the Gemini API key
# IMPORTANT: Set your Gemini API key as an environment variable named GOOGLE_API_KEY
# You can get your key from https://makersuite.google.com/app/apikey
try:
    api_key = os.environ["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.error("Please set your GOOGLE_API_KEY environment variable.")
    st.stop()

st.title("Recipe Recommender")

ingredients = st.text_input("Enter the ingredients you have on hand (separated by commas):")

if st.button("Recommend a Recipe"):
    if ingredients:
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = f"""Based on the following ingredients, what is a simple recipe I can make? Please provide the recipe name, a list of ingredients, and the step-by-step instructions.

Ingredients: {ingredients}"""
        
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"An error occurred while generating the recipe: {e}")
    else:
        st.warning("Please enter some ingredients.")
