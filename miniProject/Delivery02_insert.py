import requests, json
import cx_Oracle as cx

host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()

url = 'https://openapi.gg.go.kr/GGEXPSDLV'

for page in range(1, 36):
    params = dict(
        Type='json',
        pIndex= page,
        pSize='1000',
        KEY='d0a04c69447d4550babea5e39b590457')

    raw_data = requests.get(url = url, params=params)
    binary_data = raw_data.content
    json_data = json.loads(binary_data)
    # print(json_data)

    for jd in json_data['GGEXPSDLV'][1]['row']:
        SIGUN_NM = jd['SIGUN_NM']
        STR_NM = jd['STR_NM']
        REFINE_ROADNM_ADDR = jd['REFINE_ROADNM_ADDR']
        INDUTYPE_NM = jd['INDUTYPE_NM']
        REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT']
        REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT']

        sql = """ insert into delivery_apps (idx, sigun, str_nm, addr, indutype, latitude, longitude)
                values (seq_board_num.nextval, :sigun, :str_nm, :addr, :indutype, :latitude, :longitude) """

        try:
            cursor.execute(sql, sigun=SIGUN_NM, str_nm=STR_NM, addr=REFINE_ROADNM_ADDR, indutype=INDUTYPE_NM,
                           latitude=REFINE_WGS84_LAT, longitude=REFINE_WGS84_LOGT)
            conn.commit()
            print('1개의 레코드 입력')
        except Exception as e:
            conn.rollback()
            print('insert 실행시 오류발생', e)

conn.close()