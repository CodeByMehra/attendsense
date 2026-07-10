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

    
    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()
    
    
def teacher_screen_login():
    c1, c2 = st.columns(
        2,
        vertical_alignment="center",
        gap="xxlarge",
    )

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go Bak To Home",
            type="secondary",
            key="loginbackbtn",
            shortcut="control+backspace",
        ):
            st.session_state["login_type"] = None
            st.rerun()

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
        if st.button(
            "Register Instead",
            type="primary",
            icon=":material/passkey:",
            width="stretch",
            
        ):
            st.session_state.teacher_login_type="register"
            st.rerun()

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
        if st.button(
            "Go Bak To Home",
            type="secondary",
            key="registerbackbtn",
            shortcut="control+backspace",
        ):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("Register your teacher profile", text_alignment="center")
    st.space()
    st.space()

    teacher_username = st.text_input(
        "Enter Username",
        placeholder="eg: professor1969",
    )
    
    teacher_name = st.text_input(
        "Enter Yout Name",
        placeholder="eg: professor",
    )

    teacher_password = st.text_input(
        "Enter Your Password",
        type="password",
        placeholder="Enter Password",
    )
    
    teacher_password_confirm = st.text_input(
        "Confirm Your Password",
        type="password",
        placeholder="Enter Password",
    )

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        st.button(
            "Register now",
            icon=":material/passkey:",
            shortcut="control+Enter",
            width="stretch",
        )
    
    with btnc2:
        if st.button(
            "Login Instead",
            type="primary",
            icon=":material/passkey:",
            width="stretch",
            
        ):
            st.session_state.teacher_login_type="login"
            st.rerun()

    footer_dashboard()