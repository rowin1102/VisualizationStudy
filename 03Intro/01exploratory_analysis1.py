import pandas as pd

# csv 파일을 데이터프레임으로 변환. header옵션으로 첫행부터 사용.
df = pd.read_csv('../resData/auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'naem']

# 데이터프레임의 일부 데이터 확인
print('처음 5개 행', '='*30)
print(df.head())
print('마지막 5개 행', '='*30)
print(df.tail())

# 행의 갯수, 열의 갯수를 튜플로 반환
print('데이터프레임의 모양과 크기', '='*30)
print(df.shape)

# 클래스유형, 행 인덱스, 열의 이름과 갯수, 자료형 등을 출력
print('내용 확인', '='*30)
print(df.info())

# 데이터프레임 전체의 컬럼의 타입
print('자료형 확인1 확인', '='*30)
print(df.dtypes)

# 연비, 실린더 수 컬럼을 지정해서 타입 확인
print('자료형 확인2 확인', '='*30)
print(df.mpg.dtypes)
print(df.cylinders.dtypes)

""" 전체갯수, 평균, 표준편차, 4분위값 등의 정보를 출력"""
print('기술 통계 정보 확인1', '='*30)
print(df.describe())

print('기술 통계 정보 확인2 - include 옵션 추가 ', '='*30)
print(df.describe(include='all'))

print('자료의 갯수', '='*30)
print(df.count())
print(type(df.count()))

# 오라클의 group by와 유사하게 중복을 제거한 결과 출력
print('고유값 확인', '='*30)
# origin은 제조국을 표현하는 컬럼
unique_values = df['origin'].value_counts()
print(unique_values)