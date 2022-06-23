# 도시별 평균적 방 욕실 수를 시각화
# 도시별 평균 집사이즈 및 집사이즈에 따른 
import pandas as pd 
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = (20,10)
df = df = pd.read_csv('./realtor-data.csv')
df = df.dropna(subset=['bed', 'bath'])
df['ft price'] = 1 / df['house_size'] * df['price']
df = df.groupby(by=['state']).mean()
df.plot.bar(y=['bath', 'bed'])
plt.show()
df.plot(y=['house_size', 'ft price'])
plt.show()
print(df)