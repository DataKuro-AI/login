import streamlit as st

# 認証の状態を確認
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("このページにアクセスするにはログインが必要です。")
    st.stop()

# 認証後のページ内容を表示
st.title("ページ1")
st.write("ここはページ1のコンテンツです。")
