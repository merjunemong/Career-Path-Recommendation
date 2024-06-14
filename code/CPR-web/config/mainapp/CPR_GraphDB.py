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

    def fetch_data(self, query, parameters):
        with self.driver.session() as session:  # 세션을 생성하고 자동으로 종료되게 함
            result = session.run(query, parameters)  # 쿼리 실행
            data = [record for record in result]  # 결과를 리스트로 변환
            return data
        
    def find_job(self, user_skills):
        names = self._find_and_return_job(user_skills)
        return names

    def _find_and_return_job(self, user_skills):
        query = (
            "WITH $userSkills AS userSkills "
            "MATCH (skill:NCS)-[:HAS_JOB]->(job:KECO) "
            "WHERE skill.name IN userSkills "
            "WITH job, COUNT(skill) as matchCount "
            "ORDER BY matchCount DESC "
            "LIMIT 20 "
            "RETURN job"
        )
        
        parameters = {"userSkills": user_skills}
        
        jobs = self.fetch_data(query, parameters)
        data = [record['job']['name'] for record in jobs]

        return data
    
    def find_max_edge_skill(self, job_name):
        max_edge_skill = self._find_and_return_max_edge_skill(job_name)
        return max_edge_skill

    def _find_and_return_max_edge_skill(self, job_name):
        query = (
            "MATCH (keco:KECO {name: $job_name}) " # 직업 찾기
            "MATCH (ncs:NCS)-[:HAS_JOB]->(keco) " # 해당 직업 skill 찾기
            "WITH ncs, count(*) as connections " # skill 노드 간선 개수 count
            "ORDER BY connections DESC " # 간선 개수 내림차순으로 정렬
            #"LIMIT 5 "
            "RETURN ncs"
        )
        parameters={"job_name": job_name}
        
        result = self.fetch_data(query, parameters)
        data = [record['ncs']['name'] for record in result]  # 결과를 리스트로 변환

        return data
    
def openApp():
    scheme = "neo4j"  # Connecting to Aura, use the "neo4j+s" URI scheme
    host_name = "localhost"
    port = 7687
    uri = f"{scheme}://{host_name}:{port}"
    user = "neo4j"
    password = "cpr2024@"
    database = "neo4j"
    app = CPR_GraphDB(uri, user, password, database)
    return app

def getJob(user_skills):
    app = openApp()
    jobs = app.find_job(user_skills)
    app.close()
    return jobs

def getSkills(job_name):
    app = openApp()
    skills = app.find_max_edge_skill(job_name)
    app.close()
    return skills