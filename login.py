import streamlit as st

# ユーザー認証情報を定義
USERNAME = "abcd"
PASSWORD = "abcd"

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

# 認証の状態を確認
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# 認証されていない場合、ログインフォームを表示して処理を停止
if not st.session_state["authenticated"]:
    login()
    st.stop()  # 認証されていない場合、ここで実行を停止

# 認証された後にのみページを選択して表示
page = st.sidebar.selectbox("ページを選択してください", ["sample", "page1"])

if page == "sample":
    # Sampleページの内容を表示
    st.title("ログイン成功")
    st.write("ここはSampleページのコンテンツです。")
elif page == "page1":
    # ページ1の内容を表示
    st.title("ページ1")
    st.write("ここはページ1のコンテンツです。")
