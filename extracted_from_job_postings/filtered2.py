import pandas as pd

df = pd.read_csv("filter_skills_group_job_title*.csv") # *=번호로 대체

filtered_df = df[~df['skills'].str.contains("추출할 역량이 없습니다")]

def unique_skills(skills):
    unique_skills_set = set()
    for skill in skills:
        unique_skills_set.update([s.strip() for s in skill.split(',')])
    return ', '.join(sorted(unique_skills_set))

aggregated_df = filtered_df.groupby('job_title')['skills'].agg(unique_skills).reset_index()

print(aggregated_df)

aggregated_df.to_csv("채용공고 추출/output*.csv", index=False) # *=번호로 대체
