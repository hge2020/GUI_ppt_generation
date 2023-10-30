import streamlit as st
import json

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


with open('data.json') as f:
    data = json.load(f)

st.set_page_config(page_title="기타", page_icon="📄")

st.markdown("# 기타(중앙정렬)")

if st.sidebar.button(label = "초기화"):
    with open("data.json", "w") as f:
        json.dump({"index": 0}, f)

for key, value in data.items():
    if not key=="index":
        st.sidebar.write(value["title"])

st.write(
    """
    내용을 입력해주세요.
    """
)
txt = st.text_area(
    label="내용",
    height = 600
    )

idx = data["index"]

data[idx] = {
    'func':'GenAd_m',
    'title':txt[0:10]+"...",
    'txt':txt
}

data["index"] = idx+1
if st.button(label="추가"):
    with open("data.json", "w") as f:
        json.dump(data, f)
    st.text("done")