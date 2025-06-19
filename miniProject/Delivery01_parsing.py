import requests, json

url = 'https://openapi.gg.go.kr/GGEXPSDLV'

params = dict(
    Type='json',
    pSize='10',
    KEY='d0a04c69447d4550babea5e39b590457')

raw_data = requests.get(url = url, params=params)
binary_data = raw_data.content
json_data = json.loads(binary_data)