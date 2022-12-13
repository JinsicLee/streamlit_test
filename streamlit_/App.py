# streamlit 라이브러리 호출
import streamlit as st
import numpy as np
import pandas as pd
#import seaborn as sns

# https://docs.streamlit.io/library/get-started/main-concepts
# st.write() 마크다운

st.title(" <조> 추첨 페이지")
st.header(" 여러분의 참여를 환영합니다 :) ")
#st.image("./no_gs.jpg")

# https://docs.streamlit.io/library/cheatsheet
# 추첨 대상인 13명의 이름을 넣을 수 있는 text_input
# 3 x 4 (row, col)
# 열을 배치하는 메소드
tabs = st.tabs(['참가자','조'])
#0번째 탭에 columns(열)을 삽입
columns = tabs[0].columns(4) # 화면을 열로 나누어서 배치
# 가로 4개의 열 -> columns = [col1, col2, col3, col4]
# col1, col2, col3, col4
# enumerate : index, value
for idx, col in enumerate(columns): #열의 위치
    # 이중 For문
    # col.text_input(f"조 추첨 대상 {idx+1}", key=idx)
    for idx2 in range(4):
        # key가 겹치면 안 됨
        # col 안에 메소드를 통하여 element를 생성
        col.text_input(
            f"조 목록 {idx+1 + idx2 * 4}", 
            key=f"n{idx+1 + idx2 * 4}"
            )#4번 호출됨

columns2 = tabs[0].columns(4)
#2번째 조
#columns -> columns2 , taps[0], -> taps[1]

for idx, col in enumerate(columns2): #열의 위치
    # 이중 For문
    # col.text_input(f"조 추첨 대상 {idx+1}", key=idx)
    for idx2 in range(4):
        # key가 겹치면 안 됨
        # col 안에 메소드를 통하여 element를 생성
        col.text_input(
            f"조 목록 {idx+1 + idx2 * 4}", 
            key=f"n{idx+1 + idx2 * 4}"
            )#4번 호출됨
# <추첨 버튼>
# 13개의 짝을 지어서 표시해줄 그래픽
if st.button('추첨시작^^'):

    # 13명이 소속될 조 이름을 넣을 위치
    #st.write(st.session_state)
    #np.random.choice -> 추출해서 이름들, 목록
    # 1. st.session_state - n,g가 섞여있음
    ss = pd.Series(st.session_state)
    #st.write(ss)
    ##ss2 = ss[ss != '']
    ss2 = ss[ss.ne("")]
    #st.write(ss2)
    # contains, find  * str관련 메소드 사용할 수 있게 함
    n_idx = ss2.index.str.contains('n')
    n_data = ss2[n_idx]
    st.write(n_data)

    g_idx = ss2.index.str.contains('g')
    g_data = ss2[g_idx]
    st.write(g_data)

    # n_data를 섞여줄 것임 (비복원으로)
    n_rd = np.random.choice(n_data, len(n_data), replace=False)
    st.write(n_rd)
    g_rd = np.random.choice(g_data, len(g_data), replace=False)
    st.write(g_rd)

    # 2. df 형태로 정리
    df = pd.DataFrame({
        '추첨 대상자 이름' : n_rd,
        '조이름' : g_rd,
    })
    #st.baloon()
    st.snow()
    st.write(df)



