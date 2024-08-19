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

# 認証されていない場合、ログインフォームを表示して処理を停止
if not st.session_state["authenticated"]:
    login()
    st.stop()  # 認証されていない場合、ここで実行を停止

# 認証後にのみ表示するコンテンツ
st.title("ページ1")
st.write("ここはページ1のコンテンツです。")
