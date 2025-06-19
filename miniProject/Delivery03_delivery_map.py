import cx_Oracle as cx
import folium

host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()

sql = 'select * from delivery_apps order by idx asc'
cursor.execute(sql)

delivery_map = folium.Map(location=[37.553524, 126.984330], zoom_start=10)

input_sigun = input('시군을 입력하세요: ')

for rs in cursor:
    idx = rs[0]
    sigun = rs[1]
    str_nm = rs[2]
    addr = rs[3]
    indutype = rs[4]
    latitude = rs[5]
    longitude = rs[6]

    if sigun == input_sigun:
        folium.Marker([latitude, longitude], popup=str_nm).add_to(delivery_map)
        print(str_nm, latitude, longitude)

delivery_map.save(f"../saveFiles/delivery_map_{input_sigun}.html")
print('맵 생성')