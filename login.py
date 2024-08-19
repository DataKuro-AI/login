import streamlit as st
import importlib.util

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
        else:
            st.sidebar.error("ユーザー名またはパスワードが違います")

# 認証の状態を確認
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    st.sidebar.success("ログイン成功")

    # ページ選択のためのサイドバー
    page = st.sidebar.selectbox("ページを選択してください", ["sample", "page1"])

    # 選択されたページに応じて対応するファイルをロードして実行
    if page == "sample":
        file_to_load = "sample.py"
    elif page == "page1":
        file_to_load = "pages/page1.py"
    
    spec = importlib.util.spec_from_file_location(page, file_to_load)
    module = importlib.util.module_from_spec(spec)
    
    try:
        spec.loader.exec_module(module)
        st.write(f"{file_to_load} が正常に実行されました。")
    except FileNotFoundError:
        st.error(f"{file_to_load} が見つかりませんでした。")
    except Exception as e:
        st.error(f"エラーが発生しました: {str(e)}")
