import pandas as pd
import matplotlib.pyplot as plt

""" pie chart : 원을 파이조각처럼 나누어 표현하는 그래프로 데이터의 크기가
        클수록 파이가 크게 표현된다. """

df = pd.read_csv('../resData/auto-mpg.csv', header = None)
plt.style.use('default')

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# count라는 새로운 컬럼을 생성하고, 값 1을 일괄적으로 지정.
df['count'] = 1
""" origin은 제조국가를 표현하는 컬럼으로 1(USA), 2(EU), 3(JPN)을 의미.
    이 컬럼을 그룹화 한 후 합계(sum) 연산을 하면 각 국가변 카운트를 계산할 수 있다. """
df_origin = df.groupby('origin').sum()
print(df_origin.head())

# 제조국가 값을 실제 국가면으로 표시하기 위해 인덱스로 지정.
df_origin.index = ['USA', 'EU', 'JAPAN']

""" 합계한 결과(count컬럼)를 통해 파이차트 생성
    autopct : 퍼센트(%) 표시. 여기서는 1.2f이므로 소수 이하 둘째자리까지 표현
     startangle : 파이 조각을 나누는 시작점으로 각도 표시 """
df_origin['count'].plot(kind='pie', figsize=(7, 5), autopct='%1.2f%%',
                        startangle=10, colors=['chocolate', 'bisque', 'cadetblue'])

plt.title('Model Origin', size=20)
# 파이 차트의 비율을 원에 가깝게 조정
plt.axis('equal')
plt.legend(labels=df_origin.index, loc='upper right')

plt.show()