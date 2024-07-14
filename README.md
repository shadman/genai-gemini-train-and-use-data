# Gen AI Gemini Train and Use Data for Prompts
Web Scrape News Articles for Elections to train AI agents, use the Gemini AI model to analyze and answer queries

## Install dependencies
- pip google.generativeai
- pip install IPython
- pip install requests
- pip install beautifulsoup4

## API Key
Set Env or update API KEY on line number 12, file genai-query-with-prompt.py with yours
> GOOGLE_API_KEY="XXccss233XXcccsszX"

## Input / Predefined Text
> Tell me something about Biden and Trump debate
file: genai-query-with-prompt.py
line: 37


## Run to Train
> python genai-train.py


## Run to submit a DEFINED prompt (which you can change in code/replace with user input)
> python genai-query-with-prompt.py



## Output : (Dev Testing Output)

The text you provided focuses on the key swing states in the upcoming US election and their significance in determining the winner. It doesn't specifically mention a debate between Biden and Trump. However, it does offer some insights into their campaigns and potential strengths and weaknesses:

    * Biden's challenges: High inflation, concerns about immigration and border security, potential backlash from disillusioned African-American voters.
    * Trump's challenges: Ongoing legal battles, potential negative impact from past actions related to election interference, need to win over undecided voters in key states.

The text highlights that both candidates are campaigning aggressively in these swing states to secure victory.

To find information on Biden and Trump debates, you could:

    * Search for "Biden Trump debates" on a search engine like Google.
    * Check reputable news sources like the New York Times, CNN, or BBC for coverage of any upcoming debates.
    * Visit the official websites of the Democratic and Republican parties for announcements about debates.

Keep in mind that the text focuses on the broader political landscape, and doesn't specifically detail a Biden-Trump debate.


## Get started
- https://aistudio.google.com/app/apikey
- https://colab.research.google.com/
- https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb#scrollTo=5b4Hkfj-pm3p
