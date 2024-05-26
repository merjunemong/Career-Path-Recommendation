import logging

from neo4j import GraphDatabase, RoutingControl
from neo4j.exceptions import DriverError, Neo4jError


class CPR_GraphDB:

    def __init__(self, uri, user, password, database=None):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.database = database

    def close(self):
        # Don't forget to close the driver connection when you are finished
        # with it
        self.driver.close()

    # def create_relationship(self, job1_name, job2_name):
    #     with self.driver.session() as session:
    #         # Write transactions allow the driver to handle retries and
    #         # transient errors
    #         result = self._create_and_return_relationship(
    #             job1_name, job2_name
    #         )
    #         print("Created relationship between: "
    #               f"{result['p1']}, {result['p2']}")

    # def _create_and_return_relationship(self, job1_name, job2_name):

    #     # To learn more about the Cypher syntax,
    #     # see https://neo4j.com/docs/cypher-manual/current/

    #     # The Cheat Sheet is also a good resource for keywords,
    #     # see https://neo4j.com/docs/cypher-cheat-sheet/

    #     query = (
    #         "CREATE (p1:job { name: $job1_name }) "
    #         "CREATE (p2:job { name: $job2_name }) "
    #         "CREATE (p1)-[:KNOWS]->(p2) "
    #         "RETURN p1.name, p2.name"
    #     )
    #     try:
    #         record = self.driver.execute_query(
    #             query, job1_name=job1_name, job2_name=job2_name,
    #             database_=self.database,
    #             result_transformer_=lambda r: r.single(strict=True)
    #         )
    #         return {"p1": record["p1.name"], "p2": record["p2.name"]}
    #     # Capture any errors along with the query and data for traceability
    #     except (DriverError, Neo4jError) as exception:
    #         logging.error("%s raised an error: \n%s", query, exception)
    #         raise

    def find_job(self, job_name):
        names = self._find_and_return_job(job_name)
        print(names)
        #for name in names:
        #    print(f"Found job: {name}")

    def _find_and_return_job(self, job_name):
        query = (
            "MATCH (keco:KECO {name: $job_name})"#-[:KECO_NAME]->(subClass:KECOSubClass)-[:KECO_SUB_CLASS]->(smallClass:KECOSmallClass)-[:KECO_SMALL_CLASS]->(middleClass:KECOMiddleClass)-[:KECO_MIDDLE_CLASS]->(largeClass:KECOLargeClass)"
            "MATCH (ncs:NCS)-[:HAS_JOB]->(keco)"
            "RETURN keco, ncs"#subClass, smallClass, middleClass, largeClass, ncs"
        )
        names = self.driver.execute_query(
            query, job_name=job_name,
            database_=self.database, routing_=RoutingControl.READ#,
            #result_transformer_=lambda r: r.value("name")
        )
        return names
    
    def find_max_edge_skill(self, job_name):
        max_edge_skill = self._find_and_return_max_edge_skill(job_name)
        print(max_edge_skill)

    def _find_and_return_max_edge_skill(self, job_name):
        query = (
            "MATCH (keco:KECO {name: $job_name})" # 직업 찾기
            "MATCH (ncs:NCS)-[:HAS_JOB]->(keco)" # 해당 직업 skill 찾기
            "WITH ncs, count(*) as connections" # skill 노드 간선 개수 count
            "ORDER BY connections DESC" # 간선 개수 내림차순으로 정렬
            "LIMIT 5"
            "RETURN ncs"
        )
        result = self.driver.execute_query(
            query, job_name=job_name,
            database_=self.database, routing_=RoutingControl.READ
        )
        return result

if __name__ == "__main__":
    # For Aura specific connection URI,
    # see https://neo4j.com/developer/aura-connect-driver/ .
    scheme = "neo4j"  # Connecting to Aura, use the "neo4j+s" URI scheme
    host_name = "localhost"
    port = 7687
    uri = f"{scheme}://{host_name}:{port}"
    user = "neo4j"
    password = "cpr2024@"
    database = "neo4j"
    app = CPR_GraphDB(uri, user, password, database)
    try:
        #app.find_job("경비원")
        app.find_max_edge_skill("경비원")
    finally:
        app.close()

#Output

#EagerResult(records=[<Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7355' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '범인공격대응', 'ncs': '1101010114'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7360' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '총기탄약 유지관리', 'ncs': '1101010119'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7359' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '호송장비 운용관리', 'ncs': '1101010118'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7362' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '경보현장대응', 'ncs': '1101010121'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7354' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '총기폭발물 대응', 'ncs': '1101010113'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7344' labels=frozenset({'NCS'}) properties={'level': '4', 'name': '경비계획', 'ncs': '1101010101'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7351' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '보안관제', 'ncs': '1101010110'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7361' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '기계경비시스템 설치관리', 'ncs': '1101010120'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7363' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '장비유지관리', 'ncs': '1101010122'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7353' labels=frozenset({'NCS'}) properties={'level': '5', 'name': '경비관련법규현장적용', 'ncs': '1101010112'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7345' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '경비고객관계 관리', 'ncs': '1101010103'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7347' labels=frozenset({'NCS'}) properties={'level': '2', 'name': '출입통제', 'ncs': '1101010105'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7356' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '정보보안실행', 'ncs': '1101010115'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7350' labels=frozenset({'NCS'}) properties={'level': '2', 'name': '사건사고대처', 'ncs': '1101010108'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7364' labels=frozenset({'NCS'}) properties={'level': '5', 'name': '기계경비기획', 'ncs': '1101010123'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7357' labels=frozenset({'NCS'}) properties={'level': '5', 'name': '국가법체계교육', 'ncs': '1101010116'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7346' labels=frozenset({'NCS'}) properties={'level': '2', 'name': '경계방 비', 'ncs': '1101010104'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7348' labels=frozenset({'NCS'}) properties={'level': '2', 'name': '질서유지', 'ncs': '1101010106'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7349' labels=frozenset({'NCS'}) properties={'level': '2', 'name': '순찰활동', 'ncs': '1101010107'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7365' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '오경보관리', 'ncs': '1101010124'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7352' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '테러리즘대응', 'ncs': '1101010111'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7367' labels=frozenset({'NCS'}) properties={'level': '2', 'name': '보고문서관리', 'ncs': '1101010126'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:9308' labels=frozenset({'NCS'}) properties={'level': '5', 'name': '장비유지관리', 'ncs': '1502010109'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7358' labels=frozenset({'NCS'}) properties={'level': '3', 'name': '보안장비 운용관리', 'ncs': '1101010117'}>>, <Record keco=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:24778' labels=frozenset({'KECO'}) properties={'keco': '54201', 'name': '경비원'}> ncs=<Node element_id='4:3fa84422-df73-43ca-94a3-636cd9833bc1:7366' labels=frozenset({'NCS'}) properties={'level': '4', 'name': '사후조치', 'ncs': '1101010125'}>>], summary=<neo4j._work.summary.ResultSummary object at 0x0000020CEE1BED90>, keys=['keco', 'ncs'])