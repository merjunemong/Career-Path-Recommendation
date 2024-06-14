import os
import pandas as pd

# 현재 스크립트의 경로를 얻음
current_dir = os.path.dirname(__file__)

# crawlling 폴더의 경로
crawlling_dir = os.path.join(current_dir, 'crawlling')

# crawlling 폴더 내의 모든 CSV 파일을 읽어들여 하나로 병합
dfs = []
for file_name in os.listdir(crawlling_dir):
    if file_name.endswith('.csv'):
        file_path = os.path.join(crawlling_dir, file_name)
        df = pd.read_csv(file_path)
        dfs.append(df)

# 병합된 데이터프레임 생성
merged_df = pd.concat(dfs, ignore_index=True)

# 병합된 데이터프레임을 하나의 CSV 파일로 저장
output_file = os.path.join(current_dir, 'merged_output.csv')
merged_df.to_csv(output_file, index=False)

print(merged_df)