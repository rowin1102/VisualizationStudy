import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = '../resData/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0)
df = df.ffill()

mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
print(df_seoul.head())
df_seoul.set_index('전입지', inplace=True)

col_years = list(map(str, range(1970, 2018)))
df4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

# 데이터프레임을 전치한다. 행과 열을 바꿈.
df4 = df4.transpose()
plt.style.use('ggplot')
# 데이터프레임의 인덱스를 정수형으로 변경(map함수의 첫 번째 인수로 int함수 사용)
df4.index = df4.index.map(int)

""" 면적그래프
        kind = 'area' : 면적 그래프를 그리기 위한 옵션
        stack = False : 그래프를 겹쳐서 표현
        stack = True : 그래프를 겹치지 않게 표현
        alpha : 투명도 설정으로 0~1사이로 표현. 숫자가 작을수록 투명해짐. """
# df4.plot(kind='area', stacked=False, alphas=0.2, figsize=(20,10))
df4.plot(kind='area', stacked=True, alpha=0.2, figsize=(20,10))

plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('이동 인구 수', size=20)
plt.xlabel('기간', size=20)
plt.legend(loc='best', fontsize=15)

plt.show()