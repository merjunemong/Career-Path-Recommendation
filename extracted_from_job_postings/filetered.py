import pandas as pd

df = pd.read_csv("extract_file*.csv") # *=번호로 대체

filtered_df = df[~df['skills'].str.contains("추출할 역량이 없습니다")]

aggregated_df = filtered_df.groupby('job_title')['skills'].apply(lambda x: ', '.join(x.unique())).reset_index()

print(aggregated_df)

aggregated_df.to_csv("filter_skills_group_job_title*.csv", index=False)
