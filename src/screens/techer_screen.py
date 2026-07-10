import streamlit as st

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.ui.base_layout import (
    style_background_dashboard,
    style_base_layout,
)


def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    
    teacher_screen_login()
    
    
def teacher_screen_login():
    c1, c2 = st.columns(
        2,
        vertical_alignment="center",
        gap="xxlarge",
    )

    with c1:
        header_dashboard()

    with c2:
        st.button(
            "Go Bak To Home",
            type="secondary",
            key="loginbackbtn",
            shortcut="control+backspace",
        )

    st.header("Login using password", text_alignment="center")
    st.space()
    st.space()

    teacher_username = st.text_input(
        "Enter Username",
        placeholder="eg: professor1969",
    )

    teacher_password = st.text_input(
        "Enter Your Password",
        type="password",
        placeholder="Enter Password",
    )

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        st.button(
            "Login",
            icon=":material/passkey:",
            shortcut="control+Enter",
            width="stretch",
        )
    
    with btnc2:
        st.button(
            "Register Instead",
            type="primary",
            icon=":material/passkey:",
            width="stretch",
            
        )

    footer_dashboard()
        
    

def teacher_screen_register():
    c1, c2 = st.columns(
        2,
        vertical_alignment="center",
        gap="xxlarge",
    )

    with c1:
        header_dashboard()

    with c2:
        st.button(
            "Go Bak To Home",
            type="secondary",
            key="loginbackbtn",
            shortcut="comtrol+backspace",
        )

    st.header("Register your teacher profile")

    footer_dashboard()