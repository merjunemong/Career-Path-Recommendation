import requests
import json

def transform_data(original_data):
    grouped_data = {}
    # 데이터 그룹화 및 jobBasCompeList 생성
    for item in original_data['data']:
        compeUnitName = item['compeUnitName']
        ncsClCd_cleaned = item.get("ncsClCd", "").split("_")[0]
        if compeUnitName not in grouped_data:
            grouped_data[compeUnitName] = {
                "ncsClCd": ncsClCd_cleaned,
                "compeUnitName": compeUnitName,
                "jobBasCompeList": []
            }
        # jobBasCompeName과 jobBasCompeFactrNm을 jobBasCompeList에 추가
        grouped_data[compeUnitName]['jobBasCompeList'].append({
            "jobBasCompeName": item['jobBasCompeName'],
            "jobBasCompeFactrNm": item['jobBasCompeFactrNm']
        })

    return list(grouped_data.values())

url = 'http://apis.data.go.kr/B490007/ncsJobBase/openapi19'
service_key = 'Sc+l8WTQK8VTHuwvQI++2Ca1RacQvLETcDka/F8Dpt5amYGjMc8eHQWt9HG7yAyCjlY3XZnpR6ykCcvJZIIblQ=='

for ncsLclasCd in range(1, 25):
    params = {
        'serviceKey': service_key,
        'pageNo' : '1',
        'numOfRows' : '10000',
        'returnType': 'json',
        'ncsLclasCd': f'{ncsLclasCd:02}'  # 01, 02, ... 형식으로 맞춰주기
    }

    response = requests.get(url, params=params)
    
    # 요청이 성공했는지 확인
    if response.status_code == 200:
        try:
            data = response.json()  # 응답을 JSON으로 변환
            transformed_data = transform_data(data)  # 데이터 전처리 함수 적용
            final_json = {"data": transformed_data}  # 최종 JSON 구조로 포매팅

            # 파일에 저장
            filename = f'ncsFC_{ncsLclasCd:02}.json'
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(final_json, f, ensure_ascii=False, indent=4)
            print(f"파일이 성공적으로 생성되었습니다: {filename}")
        except json.JSONDecodeError:
            print(f"JSON decoding failed for ncsLclasCd {ncsLclasCd:02}")
    else:
        print(f"Failed to get data for ncsLclasCd {ncsLclasCd:02}, Status Code: {response.status_code}")
