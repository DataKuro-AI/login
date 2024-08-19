import streamlit as st
import importlib.util

# ユーザー認証情報を定義
USERNAME = "abcd"
PASSWORD = "abcd"

# ログインフォームを表示
def login():
    st.title("ログイン")
    username = st.text_input("ユーザー名")
    password = st.text_input("パスワード", type="password")
    
    if st.button("ログイン"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["authenticated"] = True
        else:
            st.error("ユーザー名またはパスワードが違います")

# 認証の状態を確認
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    st.success("ログイン成功")

    # ページ選択のためのセレクトボックスを表示
    page = st.selectbox("ページを選択してください", ["sample", "page1"])

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

