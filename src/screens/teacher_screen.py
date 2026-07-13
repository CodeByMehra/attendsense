import streamlit as st

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.database.db import check_teacher_exists, create_teacher, teacher_login

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()
    

def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    c1, c2 = st.columns(
        2,
        vertical_alignment="center",
        gap="xxlarge",
    )

    with c1:
        header_dashboard()

    with c2:
        st.subheader(f"""Welcome, {teacher_data['name']} """)
        if st.button(
            "Logout",
            type="secondary",
            key="teacher_logout_btn",
            shortcut="control+backspace",
        ):
            st.session_state["is_logged_in"] = False
            if "teacher_data" in st.session_state:
                del st.session_state["teacher_data"]
            st.session_state["login_type"] = None
            st.session_state["teacher_login_type"] = "login"
            st.rerun()
            
    st.space()
    
    if "current_teacher_tab" not in st.session_state:
        st.session_state.cuurent_teacher_tab = "take_attendence"
        
    tab1,tab2,tab3 = st.columns(3)
    
    with tab1:
        if st.button("Take Attendence", width="stretch", icon=":material/ar_on_you:"):
            st.session_state.cuurent_teacher_tab = "take_attendence" 
            st.rerun()

    with tab2:
        if st.button("Manage Subjects", width="stretch", icon=":material/book_ribbon:"):
            st.session_state.cuurent_teacher_tab = "manage_subject" 
            st.rerun()
             
    with tab3:
        if st.button("Attendence Records", width="stretch", icon=":material/cards_stack:"):
            st.session_state.cuurent_teacher_tab = "attendance_records" 
            st.rerun()
            
    footer_dashboard()
    
    

def login_teacher(username, password):
    if not username or not password:
        return False
    teacher = teacher_login(username, password)
    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        st.session_state["login_type"] = "teacher"
        st.session_state["teacher_login_type"] = "login"
        return True
    
    return False

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
    st.space()

    teacher_username = st.text_input(
        "Enter Username",
        placeholder="eg: professor1969",
        key="teacher_login_username",
    )

    teacher_password = st.text_input(
        "Enter Your Password",
        type="password",
        placeholder="Enter Password",
        key="teacher_login_password",
    )

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button(
            "Login",
            icon=":material/passkey:",
            shortcut="control+Enter",
            width="stretch",
            key="teacher_login_btn",
        ):
            if login_teacher(teacher_username, teacher_password):
                st.success("Welcome back!")
                st.rerun()
            else:
                st.error("Invalid username or password")
    
    with btnc2:
        if st.button(
            "Register Instead",
            type="primary",
            icon=":material/passkey:",
            width="stretch",
            key="teacher_register_nav_btn",
        ):
            st.session_state.teacher_login_type = "register"
            st.rerun()

    footer_dashboard()
        
    
def register_teacher(teacher_username, teacher_name, teacher_password, teacher_password_confirm):
    if not teacher_username or not teacher_name or not teacher_password:
        return False, "All Fields Are Required!"
    if check_teacher_exists(teacher_username):
        return False, "Username Already Taken"
    if teacher_password != teacher_password_confirm:
        return False, "Password doesn't match"
    
    try:
        create_teacher(teacher_username, teacher_password, teacher_name)
        return True, "Successfullt Created! Login Now."
    except Exception as e:
        return False, "Unexpected Error!"
    
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
        if st.button(
            "Register now",
            icon=":material/passkey:",
            shortcut="control+Enter",
            width="stretch",
        ):
            success, message = register_teacher(teacher_username, teacher_name, teacher_password, teacher_password_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)
    
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