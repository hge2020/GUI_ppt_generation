import streamlit as st
import json
import logic

st.set_page_config(
    page_title="home",
    page_icon="📔",
)

with open('data.json') as f:
    data = json.load(f)


st.write("# 예배 ppt 생성기")
if st.sidebar.button(label = "초기화"):
    with open("data.json", "w") as f:
        json.dump({"index": 0}, f)

for key, value in data.items():
    if not key=="index":
        st.sidebar.write(value["title"])

st.write('''
    예배 ppt 생성기입니다.

    각 페이지에서 순서대로 원하는 내용을 입력하고, 추가하여 전체 ppt를 생성해보세요.
    ''')

x = []

if not len(data) ==1:
    for key, value in data.items():
        if not key=="index":
            col1= st.columns([3, 1])
            with col1[0]:
                st.button(label = value["title"], use_container_width=True)
            with col1[1]:   
                x.append(st.button(label = "X", key = key))
    for i in range(len(data)-1):
        if x[i]:
            del data[f"{i}"]
            with open("data.json", "w") as f:
                json.dump(data, f)

    with open('data.json') as f:
        data = json.load(f)
    data = dict(sorted(data.items()))
    filenm = st.text_input("파일 이름을 입력하세요")
    if st.button(label="생성"):
        first = True
        for key, value in data.items():
            if not key=="index":
                if first:
                    startnm = "template.pptx"
                else:
                    startnm = filenm+".pptx"
                    logic.GenAd(startnm, filenm+".pptx", "")
                if value["func"]=="GenLyrics":
                    logic.GenLyrics(startnm, filenm+".pptx", value["title"], value["txt"])
                    first = False
                elif value["func"]=="GenBible":
                    logic.GenBible(startnm, filenm+".pptx", value["vol"], value["chap"], value["start"], value["end"])
                    first = False
                elif value["func"]=="GenAd":
                    logic.GenAd(startnm, filenm+".pptx", value["txt"])
                    first = False
                elif value["func"]=="GenAd_m":
                    logic.GenAd_m(startnm, filenm+".pptx", value["txt"])
                    first = False
                
        st.write("생성이 완료되었습니다!")