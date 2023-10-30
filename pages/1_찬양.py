import streamlit as st
import json

st.set_page_config(page_title="찬양", page_icon="🎵")

with open('data.json') as f:
    data = json.load(f)


st.markdown("# 찬양")

if st.sidebar.button(label = "초기화"):
    with open("data.json", "w") as f:
        json.dump({"index": 0}, f)

for key, value in data.items():
    if not key=="index":
        st.sidebar.write(value["title"])


st.write(
    """
    찬양 제목과 가사를 입력해주세요.

    엔터가 세 개 이상 있을 경우 문제가 발생하니 꼭 정리해주세요.
    """
)

title = st.text_input(label = "제목")
txt = st.text_area(
    label="가사",
    height = 600
    )
idx = data["index"]
data[idx] = {
    'func':'GenLyrics',
    'title':title,
    'txt':txt
}
data["index"] = idx+1
if st.button(label="추가"):
    with open("data.json", "w") as f:
        json.dump(data, f)
    st.text("done")