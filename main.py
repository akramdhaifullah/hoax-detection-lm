import streamlit as st
import google.generativeai as genai
from api import api
import re

# Configure the API key
genai.configure(api_key=api)

# Set default parameters
defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

st.title('Hoax Detection')
st.write('Validate if the information is real or not!')
final_response = None

# Create a text input for the prompt
prompt = st.text_input("Insert your information here:")
# When the 'Generate' button is pressed, generate the text
if st.button('Generate'):
    formatted_prompt = f"Validate the information below\n{prompt}\nStart your answer with 'The information is true/false.', then relevant or related paragraphs."
    response = genai.chat(messages=formatted_prompt)
    final_response = response
if final_response != None:
    if final_response.last == None:
        st.write("Sorry, I cannot determine if the information is true or not.")
    else:
        text = final_response.last

        # Find the index of the first occurrence of ". "
        separator_index = text.find(". ") + 2

        # Split the paragraph into two parts using the separator index
        first_sentence = text[:separator_index]
        rest_of_paragraph = text[separator_index:]

        # Define the regex pattern for splitting paragraphs
        # pattern = r'(?<=\w\.)\s+'

        # Split the text into paragraphs
        # paragraphs = re.split(r'(?<=\w\.)\s+', text)

        # # Print the output
        # for i, paragraph in enumerate(paragraphs, start=1):
        #     print(f"paragraph {i}:\n{paragraph}\n")
        st.write(first_sentence)
        st.write(rest_of_paragraph)

