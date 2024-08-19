import streamlit as st

# ユーザー認証情報を定義
USERNAME = "abcd"
PASSWORD = "abcd"

# 認証状態の初期化
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# ログインフォームを表示
def login():
    st.sidebar.title("ログイン")
    username = st.sidebar.text_input("ユーザー名")
    password = st.sidebar.text_input("パスワード", type="password")
    if st.sidebar.button("ログイン"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["authenticated"] = True
            st.sidebar.success("ログイン成功")
        else:
            st.sidebar.error("ユーザー名またはパスワードが違います")

# 認証が必要なページの場合はログインを求める
if not st.session_state["authenticated"]:
    login()
    st.stop()

# 認証後のコンテンツ表示
st.title("メインページ")
st.write("ログイン後のコンテンツはこちらに表示されます。")
