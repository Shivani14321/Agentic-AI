import streamlit as st
import os
from datetime import date

#from langchain_core import AIMessage, HumanMessage   #because msg we are going to mention in UI is either AImsg or Humanmsg
from src.langgraph_agenticAI.UI.uiconfigfile import Config    #Config is class

class LoadStreamLitUI:
    def __init__(self):
        self.config=Config()    #for this cofig we created ini file i.e, uiconfig.ini (text file to store configs in form of key-value pairs) like yaml config. 
        self.user_controls={}    #dictionary
        
    def initialize_session(self):
        return {
        "current_step": "requirements",
        "requirements": "",
        "user_stories": "",
        "po_feedback": "",
        "generated_code": "",
        "review_feedback": "",
        "decision": None
    }
    """ def render_requirements(self):
        st.markdown('### Requirement Submission')
        st. session_state.state["requirements"]= st.text_area(
            "Enter your Requirements:",
            height=200,
            key="req-input"
        )
        if st.button("Submit requirements", key="req-input"):
            st.session_state.state["current_step"] = " generate_User_stories" """


    def load_streamlit_ui(self):   
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False
        
        

        with st.sidebar:     #sidebar for left side code
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                # API key input
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key",
                                                                                                      type="password")
                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
                   
            
            # Use case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_controls["selected_usecase"] =="Chatbot with Tool":
                # API key input
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY API KEY",
                                                                                                      type="password")
                # Validate API key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://app.tavily.com/home")
            
            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
            
            #self.render_requirements()    #this is to load right side of the page with left sidebar
        
        return self.user_controls


