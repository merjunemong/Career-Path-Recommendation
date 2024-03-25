# Career-Path-Recommendation

## 문제정의서  
### 주제  
이력서 기반 역량 매칭을 통한 커리어 추천
### 개발 배경 및 필요성  
+ 폐쇄된 데이터 베이스
  - 현재의 커리어 패스 예측 시스템은 대부분 회사 내부의 데이터에 의존한다. 이 데이터는 종종 제한된 범위의 데이터로 인해 구직자가 자신의 능력과 잘 매칭되는 다양한 직업을 발견하는 데 한계가 있다.
+ 잠재적 역량 발굴 필요
  - 이력서에 명시적으로 제시된 역량뿐만 아니라 잠재적 역량까지 발굴할 필요가 있다.
+ 직업 추천의 정확성 향상
  - 종래의 커리어 패스 예측 기술이 제한적인 데이터 세트에 의존하기 때문에 직업 추천의 정확성과 다양성이 제한된다. 더 넓은 범위의 직업과 역량 데이터를 통해 정확성을 높일 필요가 있다.
  
### 개발 요구사항
+ 이력서 기반 역량 추출 기술
  - 이력서에서 구직자의 역량을 보다 정확하게 추출할 수 있는 알고리즘과 기술을 개발한다. 이를 통해, 개인의 명시적 및 잠재적 역량을 정확하게 식별할 수 있어야 한다.
+ 추출한 역량 기반으로 거대 언어 모델 활용
  - ChatGPT api를 fine-tunig 해서 모델이 직무 및 역량에 관련된 복잡한 쿼리에 대해 보다 정확한 응답을 할 수 있도록 한다.
+ 오픈 지식 그래프와 데이터 병합
  - 공개된 지식 그래프와, 수집된 직무 및 역량 데이터를 활용하여, 보다 광범위한 커리어 패스 정보를 포함하는 그래프 데이터베이스를 구축한다. 데이터베이스는 다양한 직업 경로와 역량 간의 관계를 명확하게 표현할 수 있어야 한다.
  - Neo4j를 사용할 예정
+ 커리어 패스 예측 기술 개발
  - 이력서 데이터와 병합된 직업 지식 그래프를 기반으로, 구직자의 현재 역량을 고려하여 커리어 패스를 예측할 수 있도록 한다.
+	예측한 커리어 패스를 기반으로 직장을 추천해주는 기술 개발
+ 시각화 도구 개발
  - React, Django 등을 이용한 시각화 페이지 개발 예정
 
### 예상 결과물
+ 이력서를 올리면 그 사람의 직무/역량을 분석해서 보여주고, 그에 직장을 추천해주는 웹사이트
  - 커리어 패스(Career Path)를 제안해주는 서비스
  -	직업 지식 그래프 DB
![image](https://github.com/JeMinMoon/Career-Path-Recommendation/assets/100757595/e1b36a9e-127d-4c1c-91fc-144c0e28cbe1)


### 개발 계획(1주 단위)
-	1주차 : 데이터 수집
-	2주차 : DB 구축, 이력서에서 역량 추출 기술 분석
-	3주차 : 이력서에서 역량 추출 기술 개발, 발전
-	4주차(중간고사 전주) : 챗GPT API Fine-Tuning
-	5주차(중간고사) : 챗GPT API Fine-Tuning
-	6주차 : 직업 별 필요 역량을 그래프 기반 DB로 구축
-	7주차 : 직업 별 필요 역량을 그래프 기반 DB로 구축, 커리어 패스 예측 기술 개발
-	8주차 : 커리어 패스 예측 기술 개발
-	9주차 : 시각화할수 있는 웹 개발
-	10주차 : 시각화할수 있는 웹 개발
-	11주차 : 시각화할수 있는 웹 개발
-	기말고사 전주 : 발표 준비
-	기말고사 : 발표
-	그 후 : 데이터 볼륨 늘리기, 정확도 향상, 프로그램 최적화, 서비스 추가
![image](https://github.com/JeMinMoon/Career-Path-Recommendation/assets/100757595/28db01e9-8de8-49af-a041-7b10e0f574d7)


### 참고자료모음
[1] 밸런스업, https://www.datasciencelabs.org/projects/Balance_Up/
[2] 밸런스업 깃, https://github.com/FarmingWon/Balance_Up 
[3] 변화하는 채용시장에 대응: 향상된 직업 매칭을 위한 직무역량 기반 임베딩, https://www.datasciencelabs.org/papers/ksc-skill-based-embedding-jobmatching/  
[4] "Prediction of Future Career Path Using Different Machine Learning Models",https://www.researchgate.net/publication/351339018_Prediction_of_Future_Career_Path_Using_Different_Machine_Learning_Models  
[5] "Career Path Prediction using Resume Representation Learning and Skill-based Matching",https://ar5iv.labs.arxiv.org/html/2310.15636  
[6] 직무 관계 사전 구축, https://medium.com/saraminlab/%EC%A7%81%EB%AC%B4-%EA%B4%80%EA%B3%84-%EC%82%AC%EC%A0%84-%EA%B5%AC%EC%B6%95-2c8014e88022  
[7] "딥러닝 기반 텍스트 임베딩을 활용한 직무 추천 모델 연구." https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=36f99cf09a701b87ffe0bdc3ef48d419&keyword=%EC%9D%B4%EB%A0%A5%EC%84%9C%20%EC%97%AD%EB%9F%89  
[8] ChatGPT 공식 API문서, https://platform.openai.com/docs/introduction  
[9] SemTabGPT:  초거대  언어모델을  사용한 지식그래프  기반  시맨틱  테이블  인터프리테이션, https://www-dbpia-co-kr.libproxy.donga.ac.kr/pdf/pdfView.do?nodeId=NODE11705333  
[10] 글로트의 야심, AI로 직원들 커리어패스를 최적화하라, https://odo.jiran.com/saas/?q=YToyOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjtzOjQ6InBhZ2UiO2k6ODt9&bmode=view&idx=12447467&t=board  
  
### 관련 오픈소스 프로젝트
- Student-Career-Prediction: This project uses Decision Trees, Naive Bayes, and Random Forest algorithms to predict the best career/course for students based on their interests. [https://github.com/loobiish/Student-Career-Prediction]
- career_path_recommendation: Developed as part of a UCL Machine Learning MSc project, this code predicts your next job title based on your CV, employing a dataset provided by Adzuna.​ [https://github.com/eddiepease/career_path_recommendation]
- student-career-area-prediction-using-machine-learning: Focused on predicting the career area for students, specifically in the computer science domain, using machine learning. It processes data collected from various sources, including LinkedIn and Google Forms.​ [https://github.com/KLGLUG/student-career-area-prediction-using-machine-learning]
- Career-Prediction-System: An industry-based project aimed at predicting careers based on user profiles. [https://github.com/hrugved06/Career-Prediction-System]
- Career-Guidance-ML-Project: A career guidance system that suggests job roles using machine learning techniques such as Decision Trees, SVM, and XGBoost, designed as part of a course project​. [https://github.com/vaishnavipatil29/Career-Guidance-ML-Project]
- Career-Path-Prediction: While detailed information wasn't available directly from the browsing session, this project is listed as related to career path prediction, indicating its relevance to the field​. [https://github.com/sarthak-sehgal/Career-Path-Prediction]
