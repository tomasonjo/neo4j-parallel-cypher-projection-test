single_rel = """

CALL algo.pageRank(
'MATCH (s:Subreddit) RETURN id(s) as id',
'MATCH (s1:Subreddit)-[r:LINK]->(s2:Subreddit)
 RETURN id(s1) as source, id(s2) as target',
{graph:'cypher'})
YIELD loadMillis,computeMillis
RETURN loadMillis,computeMillis


"""


single_rel_parallel_100k = """

CALL algo.pageRank(
'MATCH (s:Subreddit) RETURN id(s) as id',
'MATCH (s1:Subreddit)-[r:LINK]->(s2:Subreddit)
 RETURN id(s1) as source, id(s2) as target SKIP {skip} LIMIT {limit}',
{graph:'cypher',batchSize:100000})
YIELD loadMillis,computeMillis
RETURN loadMillis,computeMillis

"""
