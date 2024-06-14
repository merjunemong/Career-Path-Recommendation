import multiprocessing
import os
import traceback
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from bs4 import BeautifulSoup

# 멀티프로세스를 사용하여 페이지를 처리하는 함수
def process_page(page_url, output_file):
    driver = webdriver.Chrome()
    driver.get(page_url)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        for j in range(50):
            list_num = str(j + 1)
            notice = soup.find(id='list' + list_num)
            links = notice.find('div', class_='cp-info-in').find('a', href=True)

            link_url = links['href']
            if not link_url.startswith('http'):
                link_url = 'https://www.work.go.kr' + link_url

            employmentNoticePage(link_url, output_file)  # employmentNoticePage 함수 호출

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

    finally:
        driver.quit()

# 직업 공고 페이지를 처리하는 함수
def employmentNoticePage(link_url, output_file):
    driver = webdriver.Chrome()
    driver.get(link_url)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
        
        # 경고가 나타나면 수락
        try:
            driver.switch_to.alert.accept()
        except NoAlertPresentException:
            pass

        new_page_source = driver.page_source
        new_soup = BeautifulSoup(new_page_source, 'html.parser')

        careers = new_soup.find_all('div', class_='careers-area')
        content_list = []
        for career in careers:
            career_text = career.get_text()
            # 필요한 정보 추출
            nessessary_text = career_text.split('모집요강')
            job_posting_title = [sentence.strip() for sentence in nessessary_text[0].split('\n') if sentence.strip()]  # 제목 추출

            if job_posting_title[0] == '조회수 :':
                content_list.append(job_posting_title[2])
            else:
                content_list.append(job_posting_title[1])

            data = []
            for idx in range(1, len(nessessary_text)):
                career_text = nessessary_text[idx].split('전형방법')[0].split('근무조건')[0].split('우대조건')[0].split('전형일정')[0].split('세부모집요강')[0].split('※')[0]

                # 필요한 부분 외 제거 작업
                # 줄바꿈 문자와 탭 문자를 제거하고 텍스트를 추출
                cleaned_t = career_text.split('              ')
                if len(cleaned_t) == 1:
                    cleaned_t = career_text.split('\t')[1:]
                else:
                    cleaned_t = cleaned_t[2:]
                    for idx in range(len(cleaned_t)):
                        cleaned_t[idx] = cleaned_t[idx].split('\n\n\n\n\n')
                        if len(cleaned_t[idx]) == 1:
                            cleaned_t[idx] = cleaned_t[idx][0]
                        else:
                            cleaned_t[idx] = cleaned_t[idx][1]
                processed_data = [item.replace('\n', ' ').strip() for item in cleaned_t if not item.startswith('\n') and item.replace('\n', '').strip()]
                
                if len(processed_data) != 0:
                    data = data + processed_data
            content_list.append(data)

        # csv파일에 저장
        if len(content_list[1]) != 0:
            crawlling_result = pd.DataFrame({'job_title' : content_list[0], 'texts' : [', '.join(content_list[1])]})
        else:
            crawlling_result = pd.DataFrame({'job_title' : content_list[0], 'texts' : ['" "']})

        crawlling_result.to_csv(output_file, mode='a', header=False, index=False)

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

    finally:
        driver.quit()

if __name__ == "__main__":
    #base_url = 'https://www.work.go.kr'
    num_processes = multiprocessing.cpu_count()  # 사용 가능한 CPU 코어 수
    print(num_processes)

    # 멀티프로세싱을 사용하여 각 페이지를 병렬로 처리
    with multiprocessing.Pool(num_processes) as pool:
        for i in range(30):
            page_num = i + 1
            url = f'https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=50&keywordJobCont=N&cert=&cloDateStdt=&moreCon=more&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=1&region=&infaYn=&resultCntInfo=50&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=1&indArea=&careerTypes=&searchOn=&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=&holidayGbn=&srcKeyword=&enterPriseGbn=&academicGbnoEdu=&cloTermSearchGbn=&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=N&isEmptyHeader=&depth2SelCode=&_csrf=a401b2b7-dc7b-4611-a7d4-5d0dddd12b16&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex={page_num}&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL'
            folder_name = 'crawlling'
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            output_file = os.path.join(folder_name, f'output_{page_num}.csv')  # 페이지별로 별도의 출력 파일 사용
            crawlling_file = pd.DataFrame(columns=['job_title', 'texts'])
            crawlling_file.to_csv(output_file, header=True, index=False)

            # 각 페이지를 병렬로 처리하는 프로세스 생성
            pool.apply_async(process_page, (url, output_file))

        pool.close()
        pool.join()
