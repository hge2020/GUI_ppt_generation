import streamlit as st
import json

with open('data.json') as f:
    data = json.load(f)

st.set_page_config(page_title="성경", page_icon="📖")

st.markdown("# 성경")

if st.sidebar.button(label = "초기화"):
    with open("data.json", "w") as f:
        json.dump({"index": 0}, f)

for key, value in data.items():
    if not key=="index":
        st.sidebar.write(value["title"])

st.write(
    """
    성경 내용을 입력하세요.
    갓피아 성경에서 검색하여 입력하실 수도 있습니다.
    """
)

option = st.selectbox('입력 방식 선택하기',
                    ('검색하여 입력하기', '직접 입력하기'))

idx = data["index"]

if option == '검색하여 입력하기':
    col1= st.columns(2)
    with col1[0]:
        v = st.selectbox('구/신약', ('구약','신약'))
    with col1[1]:
        if v == '구약':
            vol = st.selectbox('권', (("창세기",
    "출애굽기",
    "레위기",
    "민수기",
    "신명기",
    "여호수아",
    "사사기",
    "룻",
    "사무엘상",
    "사무엘하",
    "열왕기상",
    "열왕기하",
    "역대상",
    "역대하",
    "에스라",
    "느헤미야",
    "에스더",
    "욥",
    "시편",
    "잠언",
    "전도서",
    "아가",
    "이사야",
    "예레미야",
    "예레미야애가",
    "에스겔",
    "다니엘",
    "호세아",
    "요엘",
    "아모스",
    "오바댜",
    "요나",
    "미가",
    "나훔",
    "하박국",
    "스바냐",
    "학개",
    "스가랴",
    "말라기")))
        elif v == '신약':
            vol = st.selectbox('권', ("마태복음",
"마가복음",
"누가복음",
"요한복음",
"사도행전",
"로마서",
"고린도전서",
"고린도후서",
"갈라디아서",
"에베소서",
"빌립보서",
"골로새서",
"데살로니가전서",
"데살로니가후서",
"디모데전서",
"디모데후서",
"디도서",
"빌레몬서",
"히브리서",
"야고보서",
"베드로전서",
"베드로후서",
"요한1서",
"요한2서",
"요한3서",
"유다서",
"요한계시록"))
    col2= st.columns(3)
    with col2[0]:
        chap = st.text_input("장")
    with col2[1]:
        start = st.text_input("시작 절")
    with col2[2]:
        end = st.text_input("끝 절")

    data[idx] = {
    'func':'GenBible',
    'title':f"{vol}{chap}:{start}-{end}",
    'vol':vol,
    'chap':chap,
    'start':start,
    'end':end
}
    data["index"] = idx+1
    if st.button(label="추가"):
        with open("data.json", "w") as f:
            json.dump(data, f)
        st.text("done")
    # if st.button(label="생성"):
    #     logic.GenBible("logic/template.pptx", "test.pptx", vol, chap, start, end)
    #     st.text("done")
elif option == '직접 입력하기':
    txt = st.text_area(
        label="Text to analyze",
        height = 600
        )
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
else:
    st.write("올바른 입력이 아닙니다.")