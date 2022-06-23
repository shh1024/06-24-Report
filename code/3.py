# 그래프 크기 설정
from matplotlib import pyplot as plt
import pandas as pd 

plt.rcParams["figure.figsize"] = (20,10)
df = pd.read_csv('realtor-data.csv', parse_dates=['sold_date'])

# sold_date 데이터가 없는 행 제거 즉 판매기록이 있는 데이터만 추출
df = df.dropna(subset=['sold_date'])

# 주 마다 판매된 숫자를 시각화
df['state'].value_counts().plot.bar(y='count')
plt.show()