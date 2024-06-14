import pandas as pd

with open('Pre_pocessed-Job-Classification.csv', encoding='utf-8') as inputfile:
    keco_df = pd.read_csv(inputfile, dtype=str)

with open('ncs-info.csv', encoding='utf-8') as inputfile:
    ncs_df = pd.read_csv(inputfile, dtype=str)
    
with open('ncs-to-keco.csv', encoding='utf-8') as inputfile:
    NtoK_df = pd.read_csv(inputfile, dtype=str)

# ncs_df, ncs_df Join
merged_df = pd.merge(ncs_df, NtoK_df, how='left', left_on=ncs_df['ncsClCd'].astype(str).str[:-2], right_on=NtoK_df['ncsClCd'].astype(str))
merged_df = merged_df.drop(columns=['key_0'])
merged_df = merged_df.drop(columns=['ncsClCd_y'])
merged_df = merged_df.rename(columns={'ncsClCd_x': 'ncsClCd'})

# keco_df 추가적으로 Join
merged_df = pd.merge(keco_df, merged_df, how='outer', left_on=keco_df['KECO'].astype(str), right_on=merged_df['KECO'].astype(str))
merged_df = merged_df.drop(columns=['key_0'])
merged_df = merged_df.rename(columns={'KECO_x': 'KECO'})
merged_df = merged_df.rename(columns={'name_x': 'name'})

# 새로운 행을 추가할 빈 DataFrame 생성
new_df = []

# 띄어쓰기를 제거한 후에 두 문자열을 비교하는 함수
def compare_strings_without_spaces(str1, str2):
    # 공백을 제거한 후에 문자열을 비교
    str1_without_spaces = str1.replace(" ", "")
    str2_without_spaces = str2.replace(" ", "")
    return str1_without_spaces == str2_without_spaces

# 각 행에 대해 조건을 검사하고, 조건에 따라 새로운 행을 바로 추가
for index, row in merged_df.iterrows():
    if pd.isna(row['KECO_y']) or row['name'] == row['name_y']:
        row['KECO'] = row['KECO'] + row['subNum']
        pass
    elif pd.isna(row['KECO']) and pd.notna(row['KECO_y']):
        row['KECO'] = row['KECO_y'] + '0'
        row['subNum'] = '0'
        row['name'] = row['name_y']
    elif pd.notna(row['KECO_y']) and compare_strings_without_spaces(row['name'], row['name_y']):
        row['KECO'] = row['KECO'] + row['subNum']
        row['name'] = row['name_y']
    elif pd.notna(row['KECO_y']) and row['name'] != row['name_y']:
        new_row = row.copy()
        new_row['KECO'] = row['KECO'] + '0'
        new_row['subNum'] = '0'
        new_row['name'] = row['name_y']
        new_df.append(new_row)
        row['KECO'] = row['KECO'] + row['subNum']
    new_df.append(row)

merged_df = pd.DataFrame(new_df)

merged_df = merged_df.drop(columns=['subNum'])
merged_df = merged_df.drop(columns=['KECO_y'])
merged_df = merged_df.drop(columns=['name_y'])

# nan 값이 없는 행에 대해서만 작업을 수행하도록 조건 추가
for index, row in merged_df.iterrows():
    if not pd.isna(row['KECO']):
        # KECO 열을 문자열로 변환하여 각 자릿수별로 분할
        merged_df.loc[index, 'KECO_Large_Class'] = row['KECO'][:1]
        merged_df.loc[index, 'KECO_Middle_Class'] = row['KECO'][:2]
        merged_df.loc[index, 'KECO_Small_Class'] = row['KECO'][:3]
        merged_df.loc[index, 'KECO_Sub_Class'] = row['KECO'][:4]

# 새로운 열을 KECO 컬럼 앞에 추가
merged_df.insert(0, 'KECO_Large_Class', merged_df.pop('KECO_Large_Class'))
merged_df.insert(1, 'KECO_Middle_Class', merged_df.pop('KECO_Middle_Class'))
merged_df.insert(2, 'KECO_Small_Class', merged_df.pop('KECO_Small_Class'))
merged_df.insert(3, 'KECO_Sub_Class', merged_df.pop('KECO_Sub_Class'))

# nan 값이 없는 행에 대해서만 작업을 수행하도록 조건 추가
for index, row in merged_df.iterrows():
    if not pd.isna(row['ncsClCd']):
        # ncsClCd 열을 문자열로 변환하여 각 자릿수별로 분할
        merged_df.loc[index, 'NCS_Large_Class'] = row['ncsClCd'][:2]
        merged_df.loc[index, 'NCS_Middle_Class'] = row['ncsClCd'][:4]
        merged_df.loc[index, 'NCS_Small_Class'] = row['ncsClCd'][:6]
        merged_df.loc[index, 'NCS_Sub_Class'] = row['ncsClCd'][:8]

# 새로운 열을 ncsClCd 열 바로 앞에 추가
merged_df.insert(9, 'NCS_Large_Class', merged_df.pop('NCS_Large_Class'))
merged_df.insert(10, 'NCS_Middle_Class', merged_df.pop('NCS_Middle_Class'))
merged_df.insert(11, 'NCS_Small_Class', merged_df.pop('NCS_Small_Class'))
merged_df.insert(12, 'NCS_Sub_Class', merged_df.pop('NCS_Sub_Class'))

#확인의 편의성을 위해 정렬
sorted_df = merged_df.sort_values(by=['KECO', 'ncsClCd'], ascending=[True, True])

# new_df = pd.DataFrame(merged_df, columns=['ncsClCd', 'compeUnitName', 'level', 'KECO', 'name'])
# new_df = pd.DataFrame(merged_df, columns=['KECO', 'subNum', 'name','ncsClCd', 'compeUnitName', 'level', 'KECO_y', 'name_y'])
final_df = pd.DataFrame(merged_df, columns=['KECO_Large_Class', 'KECO_Middle_Class', 'KECO_Small_Class', 'KECO_Sub_Class',
                                            'KECO', 'name','NCS_Large_Class', 'NCS_Middle_Class', 'NCS_Small_Class',
                                            'NCS_Sub_Class', 'ncsClCd', 'compeUnitName', 'level'])
final_df.to_csv('linked_data.csv', index=False, encoding='utf-8-sig')

with open('linked_data.csv', encoding='utf-8') as inputfile:
    result = pd.read_csv(inputfile, dtype=str)
print(result)