import pandas as pd 
from matplotlib import pyplot as plt

pd.options.display.float_format = '{:.0f}'.format
plt.figure(figsize=(20, 10))

# 연도별 판매된 물건 개수 및 가격을 시각화 
df = pd.read_csv('realtor-data.csv', parse_dates=['sold_date'])
df.dropna(subset=['sold_date'])
df['sold_date'] = df['sold_date'].dt.year
df['price ft'] = (1 / df['house_size'] * df['price'])
df = df.groupby(by=['sold_date'])
plt.plot(df.size(), marker='*', color='b', label='number of sold')
plt.plot(df['price ft'].mean(), label='avg of price', marker='*', color='c')

leg = plt.legend(loc='best')

plt.show()