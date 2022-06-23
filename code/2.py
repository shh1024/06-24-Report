import pandas as pd 

# 출력 소수점에 대한 정의
pd.options.display.float_format = '{:.2f}'.format

# csv 불러오기 
df = pd.read_csv('./realtor-data.csv')

# 행에 subset에 담긴 열의 데이터가 없다면 그 행 자체를 삭제(데이터 잔처리)
df = df.dropna(subset=['price', 'house_size'])

# 집 크기 별로 집 가격은 다르므로 1ft당 가격을 측정
df['ft price'] = 1 / df['house_size'] * df['price']

df = df.drop(['price', 'acre_lot', 'house_size', 'bed', 'bath', 'zip_code'], axis=1)
df = df.sort_values(by=['state', 'city', 'street', 'ft price']).groupby(by=['state','city', 'street']).mean()
print(df.head(10))