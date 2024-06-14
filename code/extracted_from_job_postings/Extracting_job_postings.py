import pandas as pd
from openai import OpenAI
import os

#API 키 설정

client = OpenAI()
df = pd.read_csv("채용공고 추출/merged_output05_05.csv")
df = df.iloc[4000:5000]  #1000개씩
results = []

for index, row in df.iterrows():
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "너는 주어진 text에서 직업명과 역량을 추출할거야. 직업명은 고용 형태가 아닌 업무의 복잡성 및 기술 요구하는 직업명을 추출하고, 직업의 범주인 직업명만을 하나 출력해. 그리고 역량은 해당 직업의 기술이나 역량으로 분류되는 것들을 추출해. 기술적 역량을 판단할 때는 직업명과 관련된 특정 기술 용어도 역량으로 간주해서 추출해. 이때 주역량으로 분류될게 없다면 \"추출할 역량이 없습니다\"로 표기해. 이때 경력, 학력, 주소, 조직에서 제공하는 혜택, 기념 행사와 관련된 정보들은 꼭 배제해줘. 역량이 2개 이상일 경우 한 줄에 열거해. 최종 출력은 '직업명: [직업명]' \n '역량: [역량]' 형태로만 출력해.",
                },
                {
                    "role": "user",
                    "content": row['texts']+", "+row['job_title']
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )        
        job_title_skills = response.choices[0].message.content
        job_title = job_title_skills.split("직업명: ")[1].split("\n")[0].strip()
        skills = job_title_skills.split("역량: ")[1].strip()

        results.append({
            "job_title": job_title,
            "skills": skills
        })
        print(f"Success processing row {index}")
    except Exception as e:
        print(f"Error processing row {index}: {e}")
        
results_df = pd.DataFrame(results)
results_df.to_csv("extract_file5.csv", index=False)