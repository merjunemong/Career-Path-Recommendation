user_skills = ["사후조치", "장비유지관리", "총기폭발물 대응", "보고문서관리"]

def recommend_jobs(request):
    
    # 겹치는 skill 수 count
    query = """
    WITH $userSkills AS userSkills
    MATCH (skill:NCS)-[:HAS_JOB]->(job:KECO)
    WHERE skill.name IN userSkills
    RETURN job, COUNT(skill) AS matchCount
    ORDER BY matchCount DESC
    LIMIT 20
    """

    # # jaccard similarity  -> neo4j에 APOC플러그인 설치 필요
    # query = """
    # WITH $userSkills AS userSkills
    # MATCH (job:KECO)-[:HAS_JOB]->(skill:NCS)
    # WITH job, COLLECT(skill.name) AS jobSkills, userSkills
    # WITH job, jobSkills,
    #  apoc.coll.toSet(userSkills) AS userSkillSet,
    #  apoc.coll.toSet(jobSkills) AS jobSkillSet
    # WITH job, userSkillSet, jobSkillSet,
    #  apoc.coll.intersection(userSkillSet, jobSkillSet) AS intersection,
    #  apoc.coll.union(userSkillSet, jobSkillSet) AS union
    # RETURN job, 1.0 * size(intersection) / size(union) AS jaccard_similarity
    # ORDER BY jaccard_similarity DESC
    # LIMIT 10
    # """
    
    params = {"userSkills": user_skills}
    
    results, meta = db.cypher_query(query, params)
    
    jobs = []
    for job, match_count in results:
        jobs.append({
            "name": job["name"],
            "matchCount": match_count
        })
    
    return JsonResponse({'recommended_jobs': jobs})