![image](https://github.com/JeMinMoon/Career-Path-Recommendation/assets/100757595/088f310f-1bb3-419c-a3e1-dcf12b07158c)

NCS번호는 위 사진과 같이 구성되어있으며, 우린 그 중 개발연도와 버전을 제외한 나머지 부분을 사용할 예정

<KECO>

## ncs-info.csv
- ncsClCd(NCS번호),compeUnitName(능력명),level(수준)으로 구성
- 수준은 산업현장 직무의 수준을 나타내며, 직업 추천 시 본인의 역량에 맞는 수준을 추천할 때 이용 가능할 수도 있을거라 판단하여 남겨둠. 자세한 내용은 [NCS구성](https://ncs.go.kr/th01/TH-102-001-03.scdo)참조
- 기존 데이터셋의 시간 컬럼은 활용 용도 및 판단 기준을 알수 없어서 제외

## Pre-processed-Job-Classification.csv
- KECO(KECO번호),subNum(세세분류),name(직업명)으로 구성
- KECO는 대분류, 중분류, 소분류, 세분류 로 총 4자리로 구성되어 있음
- 우리가 찾은 워크넷에서 제공하는 직업분류에는 세세분류 까지 총 5자리로 구성되어 있기 때문에 KECO 4자리와 세세분류 한자리를 구분하여 컬럼 형성함

## nsc-to-keco.csv
- ncsClCd(NCS번호),KECO(KECO번호),name(직업명)으로 구성
- 기존 데이터셋의 NCS에 대한 정보가 대분류, 중분류, 소분류, 세분류 만 있고 능력단위가 없어 데이터의 길이가 8임(기존은 10). 한가지 직업을 위해 여러가지 능력이 필요하다는 뜻이므로 추천을 위해 매칭할 때 묶어서 생각할 것.

## ncsFC_01~24.json
- ncsLclasCd(대분류코드), ncsLclasCdnm(대분류코드명), ncsMclasCd(중분류코드), ncsMclasCdnm(중분류코드명), ncsSclasCd(소분류코드), ncsSclasCdnm(소분류코드명), ncsSubdCd(세분류코드), ncsSubdCdnm(세분류코드명)들은 ncsClCd(NCS번호)로 접근이 가능하여 제거
- ncsClCd(NCS번호)의 (ex.00101010101_17v2) 값 같은 경우 '_'부터의 년도, 버전 정보는 불필요하여 제거
- jobBasCompeName(직업기초능력명칭)과 jobBasCompeFactrNm(직업기초능력요소명)컬럼의 경우 공통된 compeUnitName(능력단위명칭)컬럼을 가지고 있어 jobBasCompeList(직업기초능력리스트)라는 리스트를 따로 만들어 compeUnitName(능력단위명칭)컬럼명으로 묶어 데이터를 압축함
- 마지막행에 있던 dataInfo 컬럼도 제거하여 데이터가 일관되게하였음
