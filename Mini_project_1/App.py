import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly.express as px

# 서울시의 모기 파악하기
## 모기예보제와 일자별 날씨 데이터를 통한 모기 발생 빈도 변화 파악

st.image("https://news.seoul.go.kr/welfare/files/2020/02/62cfc9f3f36041.41905113-1086x1536.jpg")
st.write("http://data.seoul.go.kr/dataList/OA-13285/S/1/datasetView.do#")

# UTF-8 / CP-949
# https://seong6496.tistory.com/269
st.write("Read Data List 1 >>")

df = pd.read_csv('./Mini_project_1/mosquito.csv', encoding='cp949')
df['발생일']=pd.to_datetime(df['모기지수 발생일'], infer_datetime_format=True)
st.write(df)

st.write("Read Chart 1 >>")

# df.describe()
# df.info()
# lp_1 = sns.lineplot(data=df, x='모기지수 발생일',y='모기지수(수변부)')
# # df.plot(x='발생일', y='모기지수(수변부)')
# # df.plot(x='발생일', y='모기지수(주거지)')
# # df.plot(x='발생일', y='모기지수(공원)')
# plt.show()
