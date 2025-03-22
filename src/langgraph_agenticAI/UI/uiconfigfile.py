from configparser import ConfigParser  #class to parse cofig text file

class Config:    #inside any class, we start with constructor
    def __init__(self,config_file="./src/langgraph_agenticAI/UI/uiconfigfile.ini"):
        self.config=ConfigParser()   #initialize the constructor, config is public variable , use this configParser object will read the config file and store in config variable
        self.config.read(config_file)

    def get_llm_options(self):    #to only read llm field from config file
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")   #DEFAULT is root note for all the below node hving access of everything written below
        
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")