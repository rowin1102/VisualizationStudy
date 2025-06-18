import folium
import pandas as pd

""" folium library : 데이터를 지도로 시각화 해주는 library.
        코드를 실행하면 IDE에서 직접 지도가 표시되지 않고, HTML 파일로 저장되어
        웹브라우저를 통해 확인해야 한다. 웹서버(Tomcat 등)가 있다면 특정 경로에
        저장하여 Spring(혹은 JSP)와 연동할 수 있다. """

# 맴표시 : 인수로 시설물의 위도/경도와 줌 레벨을 지정
seoul_map1 = folium.Map(location=[37.55, 126.98], zoom_start=12)
seoul_map1.save('../saveFiles/seoul1.html')

# tiles 옵션으로 산악지형 강조, 도로망 강조와 같은 표현이 가능.

df = pd.read_excel('../resData/서울지역_대학교_위치.xlsx', engine='openpyxl')
df.columns = ['학교명', '위도', '경도']

# 데이터프레임에 저장된 개수만큼 반복하여 지도에 마커 추가
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    # 위경도는 리스트로 부여하고, popup(풍선도움말)은 학교명 지정
    folium.Marker([lat, lng], popup=name).add_to(seoul_map1)
# 마커가 추가된 Map을 HTML파일로 저장
seoul_map1.save('../saveFiles/seoul_colleges1.html')

# 원형마커 및 추가 옵션 지정
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.CircleMarker([lat, lng], radius=10, color='brown', fill=True,
                        fill_color='coral', fill_opacity=0.7, popup=name).add_to(seoul_map1)
seoul_map1.save('../saveFiles/seoul_colleges2.html')