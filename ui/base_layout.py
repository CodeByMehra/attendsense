import streamlit as st

def style_background_home():

    st.markdown("""
                <style>
                        .stApp{
                            background: #5865F2 !important;
                        }
                </style>

                """,unsafe_allow_html=True)
    
def style_backgrounddashboard():

    st.markdown("""
                <style>
                        .stApp{
                            background: ##E0E3FF !important;
                        }
                </style>
 
                """,unsafe_allow_html=True)
    
def style_base_layout():
    st.markdown("""
            <style>
                  /* Hide top bar of streeamlit */   
                    #MainMenu,
                    footer,
                    header {
                    display: none;
                    }
                    }   
            </style>
 
                """,unsafe_allow_html=True)