import requests
import json

def transform_data(original_data):
    grouped_data = {}
    # 데이터 그룹화 및 jobBasCompeList 생성
    for item in original_data['data']:
        compeUnitName = item['compeUnitName']
        if compeUnitName not in grouped_data:
            grouped_data[compeUnitName] = {
                "ncsClCd": item.get("ncsClCd", "").split("_")[0],
                "compeUnitName": compeUnitName,
                "jobBasCompeList": []
            }
        # jobBasCompeName과 jobBasCompeFactrNm을 jobBasCompeList에 추가
        grouped_data[compeUnitName]['jobBasCompeList'].append({
            "jobBasCompeName": item['jobBasCompeName'],
            "jobBasCompeFactrNm": item['jobBasCompeFactrNm']
        })

    # 최종 데이터를 리스트로 변환
    final_data = list(grouped_data.values())
    return final_data

# API 요청
url = 'http://apis.data.go.kr/B490007/ncsJobBase/openapi19'
params = {
    'serviceKey' : '사용자키', 
    'pageNo' : '1', 
    'numOfRows' : '10000', 
    'returnType' : 'json', 
    'ncsLclasCd' : '24'
}

response = requests.get(url, params=params)
json_data = response.content
data = json.loads(json_data)

# 데이터 변환
transformed_data = transform_data(data)

# 최종 데이터를 "data" 키로 묶음
final_json = {"data": transformed_data}

# 파일에 변환된 데이터 저장
with open('ncsFC_24.json', 'w', encoding='utf-8') as f:
    json.dump(final_json, f, ensure_ascii=False, indent=4)

print("파일이 성공적으로 생성되었습니다: ncsFC_24.json")

