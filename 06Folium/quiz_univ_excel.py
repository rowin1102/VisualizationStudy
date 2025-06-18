import pandas as pd
import cx_Oracle as cx

df = pd.read_excel('../resData/전문및대학교현황.xls', engine='xlrd')

host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()

# 데이터프레임을 통해 반복할때는 iterrows() 함수가 필요.
for idx, row in df.iterrows():
    SIGUN_NM = row['시군명']
    FACLT_NM = row['시설명']
    REFINE_LOTNO_ADDR = row['소재지도로명주소']
    REFINE_WGS84_LAT = row['WGS84위도']
    REFINE_WGS84_LOGT = row['WGS84경도']

    sql = """ insert into g_univ (idx, sigun, faclt, addr, latitude, longitude)
                values (seq_board_num.nextval, :sigun, :faclt, :addr, :latitude, :longitude) """

    try:
        cursor.execute(sql, sigun=SIGUN_NM, faclt=FACLT_NM, addr=REFINE_LOTNO_ADDR,
                       latitude=REFINE_WGS84_LAT, longitude=REFINE_WGS84_LOGT)
        conn.commit()
        print('1개의 레코드 입력')
    except Exception as e:
        conn.rollback()
        print('insert 실행시 오류발생', e)

conn.close()