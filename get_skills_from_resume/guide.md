# need to setup
## PyPDF2
pdf를 text로 바꿀 수 있는 python 라이브러리이다.  
### install
```
pip install pypdf2
```
## OpenAI Python library
openai api를 사용하기 위한 라이브러리이다.
### install
```
pip install --upgrade openai
```
### 환경변수 설정
https://platform.openai.com/docs/quickstart  
내PC 우클릭-> 속성-> 고급 시스템 설정-> 환경변수-> 시스템 변수 새로 만들기  
변수명: OPENAI_API_KEY  
변수값: openai에서 발급받은 키  

# 결과
## 이력서를 pdf에서 text로 변환
![image](https://github.com/JeMinMoon/Career-Path-Recommendation/assets/100738519/788e79b9-1a49-46e6-84f4-cc5d9f13b56b)
## 변환된 이력서에서 역량 추출한 뒤 list에 저장
![image](https://github.com/JeMinMoon/Career-Path-Recommendation/assets/100738519/8539f1f0-b220-4826-889b-627088f63634)
