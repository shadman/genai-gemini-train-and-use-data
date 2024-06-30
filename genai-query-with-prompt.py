import requests
import textwrap
import csv
import random
import pandas as pd
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY = '34234234234234cxzxdfsfcvcxb' 
genai.configure(api_key=GOOGLE_API_KEY)


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# Preprocesses CSV data to extract relevant text for prompts.
def preprocess_data(csv_file):
  # Read the CSV file
  data = pd.read_csv(csv_file)

  # Choose a suitable text field or logic to extract prompts (modify based on your data)
  prompts = data["Content"].tolist()  # Example: assuming a "text_field" column

  return prompts



# Input
query = "Tell me something about Biden and Trump debate"

# Use CSV file path
csv_file = './us_elections.csv'

# Preprocess CSV data to get prompts
prompts = preprocess_data(csv_file)

# Generate content using prompts (consider iterating through prompts for multiple responses)
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(random.choice(prompts) + " " + query)

# Display the response (optional formatting)
print(response.text)
#to_markdown(response.text) # You can use to_markdown() here if desired for Markdown output
