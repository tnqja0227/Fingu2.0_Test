import os
import gradio as gr
from langchain.chains import ConversationChain
from langchain.llms import OpenAI

#  Load your OpenAI API key from environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def load_chain():
    if OPENAI_API_KEY:
        llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
        chain = ConversationChain(llm=llm)
        return chain
    else:
        return None  # Placeholder if no API key

# ... (Rest of your Gradio interface & chat bot code from previous examples) 
