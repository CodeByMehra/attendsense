import streamlit as st
import numpy as np

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.ui.base_layout import style_background_dashboard, style_base_layout

from PIL import Image
def student_screen():
    style_background_dashboard()
    style_base_layout()
    
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
    st.header("Login using Face ID", text_alignment="center")
    st.space()
    st.space()
    
    photo_source = st.camera_input("Position Your Face In Center")
    
    if photo_source:
        np.array()
    footer_dashboard(Image.open(photo_source))
