import requests
import xmltodict
import json
from pprint import pprint

#flask data 생성
def get_corona19_data(startCreateDt, endCreateDt):
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"

    parameters = {
        'serviceKey' : '11B+baCVeti1bKUYgT+l0i6afy4ClEMu6p6abG9WDbO6Zg5DHeuZ4cG0Ha5LVGmm7JswPrQRNJXb34soKy5i0A==',
        'pageNo' : '1',
        'numOfRows' : 30,
        'startCreateDt' : startCreateDt,  #시작날짜
        'endCreateDt' : endCreateDt       #끝나는날짜

        }

    res = requests.get(url, params=parameters)
    #print(res.url)
    #print(res.text)

    #xml to dict data
    dict_data = xmltodict.parse(res.text)
    #print(dict_data)

    # dict data to json
    json_data = json.dumps(dict_data)
    #print(json_data)

    #json to dict
    dict_data = json.loads(json_data)
    #pprint(dict_data['response']['body']['items']['item'])


    #for error 방지 -> totalcount 0이면 false 표기
    totalCount = dict_data['response']['body']['totalCount']
    if totalCount == '0':   #totalCount type = string 이므로 0이 아닌 '0' 삽입
        return False


    #지역정보 리스트
    local_data = dict_data['response']['body']['items']['item']
    local_data.reverse() #역행된거 바꿔주기
    #print(local_data)

    return local_data