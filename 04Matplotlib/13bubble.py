import pandas as pd
import matplotlib.pyplot as plt

""" 버블차트(Bubble chart) : 실린더 개수를 나타내는 정수를 해당 열의
        최대값 대신 상대적 크기를 나타내는 비율로 계산해서 점의 크기를 다르게 표시한다.
        점의 모양이 비눗방울 같다고 해서 '버블차트'라고 부른다. """
plt.style.use('default')

df = pd.read_csv('../resData/auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# 실린더 개수의 상대적 비율을 계산해서 시리즈로 생성한다.
cylinders_size = df.cylinders / df.cylinders.max() * 300
print(cylinders_size)

""" c : 점의 컬러
    s : 점의 크기
    alpha : 투명도
    marker : 마커의 모양
    cmap : 색깔을 정하는 컬러맵 """
df.plot(kind='scatter', x='weight', y='mpg', c='coral', s=cylinders_size,
        figsize=(10, 5), alpha=0.3, marker='o', cmap='viridis')

plt.title('Scatter Plot : mpg - weight - cylinders')

# 출력된 그래프를 png 파일로 저장한다. 이 경우 배경은 흰색으로 지정된다.
plt.savefig('../saveFiles/scatter.png')
# transparent 옵션으로 배경색을 투명하게 지정한다.
plt.savefig('../saveFiles/scatter_transparent.png', transparent=True)

plt.show()
