agg_date_rel = """

CALL algo.pageRank(
'MATCH (s:Subreddit) RETURN id(s) as id',
'MATCH (s1:Subreddit)-[r:LINK]->(s2:Subreddit)
 WHERE r.date.year = 2016
 RETURN id(s1) as source, id(s2) as target, count(*) as weight',
{graph:'cypher', weightProperty:'weight'})
YIELD loadMillis,computeMillis
RETURN loadMillis,computeMillis


"""


agg_date_rel_parallel_100k = """

CALL algo.pageRank(
'MATCH (s:Subreddit) RETURN id(s) as id',
'MATCH (s1:Subreddit)-[r:LINK]->(s2:Subreddit)
 WHERE r.date.year = 2016
 RETURN id(s1) as source, id(s2) as target, count(*) as weight SKIP {skip} LIMIT {limit}',
{graph:'cypher',batchSize:100000, weightProperty:'weight'})
YIELD loadMillis,computeMillis
RETURN loadMillis,computeMillis

"""
