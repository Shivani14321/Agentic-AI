import streamlit as st
import os
from datetime import date

from langchain_core import AIMessage, HumanMessage   #because msg we are going to mention in UI is either AImsg or Humanmsg
from src.langgraph_agenticAI.UI.uiconfigfile import Config    #Config is class
class LoadStreamLitUI:
    def __init__(self):
        self.config=Config()    #for this cofig we created ini file i.e, uiconfig.ini (text file to store configs in form of key-value pairs) like yaml config. 
        self.user_controls={}


