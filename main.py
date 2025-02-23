from templates.index import Index
import streamlit as st
from auth_view import render_login, render_register

def main():
    st.set_page_config(page_title='Sistema de Agenda', page_icon='📅', layout='centered')

    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.user_type = None
        st.session_state.user_name = ''

    if st.session_state.authenticated:
        st.sidebar.write(f'👤 Usuário: {st.session_state.user_name} ({st.session_state.user_type})')
        if st.sidebar.button('Logout'):
            st.session_state.authenticated = False
            st.session_state.user_type = None
            st.session_state.user_name = ''
            st.experimental_rerun()
        st.write('Bem-vindo ao sistema!')
        
    else:
        auth_option = st.radio('Escolha uma opção:', ['Login', 'Cadastro'])
        if auth_option == 'Login':
            render_login()
        else:
            render_register()

if __name__ == "__main__":
    Index.main()
