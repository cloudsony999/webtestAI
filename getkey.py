import google.generativeai as ai

import os
from dotenv import find_dotenv,load_dotenv

'''
def getkey(r):
    #load_dotenv(find_dotenv(),override=True)
    return r
'''
def runPrompt(key,prompt):
    print('.......the key is ...........',key)
    ai.configure(api_key=os.environ.get(key))
    model=ai.GenerativeModel('gemini-1.0-pro-latest')
    response=model.generate_content(prompt)
    return response.text
