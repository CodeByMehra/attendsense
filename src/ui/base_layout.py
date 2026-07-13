import streamlit as st

def style_background_home():

    st.markdown("""
                <style>
                        .stApp{
                            background: #5865F2 !important;
                        } 
                        .stApp div[data-testid="stColumn"]{
                        background-color:#E0E3FF !important;
                        padding:2.5rem !important;
                        border-radius: 5rem !important;
                        }
                </style>

                """,unsafe_allow_html=True)
    
def style_background_dashboard():

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
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
            
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
            
                  /* Hide top bar of streeamlit */   
                    #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }
        
        .block-container{
            padding-top:1.5rem !important;
        }
        
        h1 {
            font-family: "Climate Crisis", sans-serif !important;
            font-size: 3.5 rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: #E0E3FF;
        }
        h2 {
            font-family: "Climate Crisis", sans-serif !important;
            font-size: 1.5rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
        }
        
        h3, h4, p{
            font-family: "outfit", sans-serif !important;
        }
        button[kind="primary"]{
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }
        button[kind="secondary"]{
            border-radius: 1.5rem !important;
            background-color: #EB459E !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }
        
        button[kind="tertiary"]{
            border-radius: 1.5rem !important;
            background-color: black !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }
        
        button:hover{
            transform: scale(1.05)
        }


                      
            </style>
 
                """,unsafe_allow_html=True)