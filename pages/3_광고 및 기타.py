import streamlit as st
import json

with open('data.json') as f:
    data = json.load(f)

st.set_page_config(page_title="기타", page_icon="📄")

st.markdown("# 광고 및 기타(좌측정렬)")

if st.sidebar.button(label = "초기화"):
    with open("data.json", "w") as f:
        json.dump({"index": 0}, f)

for key, value in data.items():
    if not key=="index":
        st.sidebar.write(value["title"])

st.write(
    """
    광고 및 기타 내용을 입력해주세요.
    """
)
txt = st.text_area(
    label="내용",
    height = 600
    )

idx = data["index"]

data[idx] = {
    'func':'GenAd',
    'title':txt[0:10]+"...",
    'txt':txt
}

data["index"] = idx+1
if st.button(label="추가"):
    with open("data.json", "w") as f:
        json.dump(data, f)
    st.text("done")