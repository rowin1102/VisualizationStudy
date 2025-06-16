import io

import pandas as pd
import requests

df1 = pd.read_json('../resData/sample.json')
print(df1)

print('='*30)

# 인덱스만 출력
print(df1.index)
# 라벨형 인덱스를 통해 요소에 접근
print('마지막데이터:', df1.loc['Paul', 'c++'])
# 컬럼 전체를 출력시에는 데이터프레임명만 사용
print('첫 번째 컬럼:')
print(df1['algol'])
# 행 전체를 출력시에는 loc(iloc)를 사용
print('첫 번째 행:')
print(df1.loc['Jerry'])

print('='*30)

# 웹 URL을 지정하여 페이지의 정보를 얻어온다.
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
# 응답코드가 200이면 정상 접속된 상태이므로 JSON 데이터를 얻어온 후 데이터프레임으로 변환
if response.status_code == 200:
    jsonData = response.text
    df2 = pd.read_json(io.StringIO(jsonData))
    # id 컬럼을 인덱스로 지정 후 원본에 저장
    df2.set_index('id', inplace=True)
    print(df2)
else:
    print('API 연동 중 오류발생')
    print(response.status_code)