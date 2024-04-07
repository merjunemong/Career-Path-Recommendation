#하나씩 요청
import requests
import json

url = 'http://apis.data.go.kr/B490007/ncsJobBase/openapi19'
params ={'serviceKey' : '사용자키', 'pageNo' : '1', 'numOfRows' : '10000', 'returnType' : 'json', 'ncsLclasCd' : '09'}

response = requests.get(url, params=params)
# print(response.content)

json_data = response.content
data = json.loads(json_data)

with open('output_9.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("파일이 성공적으로 생성되었습니다: output.json")

#한번에 요청
# import requests
# import json

# url = 'http://apis.data.go.kr/B490007/ncsJobBase/openapi19'
# service_key = 'Sc+l8WTQK8VTHuwvQI++2Ca1RacQvLETcDka/F8Dpt5amYGjMc8eHQWt9HG7yAyCjlY3XZnpR6ykCcvJZIIblQ=='

# for ncsLclasCd in range(1, 24):
#     params = {
#         'pageNo' : '1',
#         'numOfRows' : '10000',
#         'serviceKey': service_key,
#         'returnType': 'json',
#         'ncsLclasCd': f'{ncsLclasCd}'
#     }

#     response = requests.get(url, params=params)
#     json_data = response.content
#     data = json.loads(json_data)

#     filename = f'output_{ncsLclasCd}.json'
#     with open(filename, 'w', encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)

#     print(f"파일이 성공적으로 생성되었습니다: {filename}")

#dataFrame으로 확인
# import pandas as pd
# import json

# # JSON 파일 불러오기
# for ncsLclasCd in range(1, 25):
#     filename = f'output_{ncsLclasCd}.json'
#     with open(filename, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     # DataFrame으로 변환
#     df = pd.DataFrame(data['data'])

#     # DataFrame 출력
#     print(df)