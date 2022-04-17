"""This file is the framework for generating multiple streamlit applications
through an object oriented framework
"""
import streamlit as st

class MultiPage:
    """Framework combining multiple streamlit apps"""
    
    def __init__(self):
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.pages =[]
    
    def add_page(self, title, func):
        """Class method to Add pages to the project
        
        Args:
            title ([str]): The title of the page we are adding to the list of apps
            
            func: Python function to render this page in streamlit
        """
        self.pages.append(
            {"title":title, 
             "function": func}
            )

    def run(self):
        #Dropdown to select the page to run
        page = st.sidebar.selectbox(
            label = "App Navigation",
            options = self.pages,
            format_func = lambda page: page['title']            
        )
        
        #run the app function
        page['function']() 