import pandas as pd

with open('직업세세분류.csv') as inputfile:
    df = pd.read_csv(inputfile, encoding='utf-8')

data = []

for index, row in df.iterrows():
    code = str(row['KNOW직업대분류']) + str(row['KNOW직업중분류']) + str(row['KNOW직업소분류']) + str(row['KNOW직업세분류'])
    data.append([code, row['KNOW직업세세분류'], row['KNOW직업명']])

new_df = pd.DataFrame(data, columns=['KECO', 'subNum', 'name'])

new_df.to_csv('Pre_pocessed-Job-Classification.csv', index=False, encoding='utf-8-sig')


with open('한국산업인력공단_국가직무능력표준 정보_20231129.CSV') as inputfile:
    df = pd.read_csv(inputfile, encoding='utf-8')

data = []

for index, row in df.iterrows():
    code = str(row['분류번호']).split('_')[0]
    data.append([code, row['명칭'], row['수준']])

new_df = pd.DataFrame(data, columns=['ncsClCd', 'compeUnitName', 'level'])

new_df.to_csv('ncs-info.csv', index=False, encoding='utf-8-sig')


with open('NCS_KECO_연계표.CSV') as inputfile:
    df = pd.read_csv(inputfile, encoding='utf-8')

data = []

for index, row in df.iterrows():
    code = str(row['대분류(NCS)']).split('.')[0] + str(row['중분류(NCS)']).split('.')[0] + str(row['소분류(NCS)']).split('.')[0] + str(row['세분류(NCS)']).split('.')[0]

    # 문자열 변환 후 길이가 3보다 작으면 앞에 0 추가
    processed_number = str(row['코드(KECO)']).replace('.0', '')
    processed_number = processed_number.zfill(4)

    data.append([code, processed_number, row['세분류(KECO)']])

new_df = pd.DataFrame(data, columns=['ncsClCd', 'KECO', 'name'])

new_df.to_csv('ncs-to-keco.csv', index=False, encoding='utf-8-sig')

with open('ncs-to-keco.CSV', encoding='utf-8-sig') as inputfile:
    df = pd.read_csv(inputfile)
    print(df)
