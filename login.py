import streamlit as st

# シンプルな認証スクリプト
USERNAME = "abcd"
PASSWORD = "abcd"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def login():
    st.title("ログイン")
    username = st.text_input("ユーザー名")
    password = st.text_input("パスワード", type="password")
    if st.button("ログイン"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["authenticated"] = True
        else:
            st.error("ユーザー名またはパスワードが違います")

if not st.session_state["authenticated"]:
    login()
    st.stop()

st.title("認証後のコンテンツ")
st.write("ここは認証に成功した後のページです。")
