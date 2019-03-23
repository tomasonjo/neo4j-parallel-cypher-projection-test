from neo4j.v1 import GraphDatabase
from single_rel_queries import single_rel, single_rel_parallel_100k
from aggregate_rel_queries import agg_rel, agg_rel_parallel_100k
from aggregate_filter_rel_queries import agg_filter_rel, agg_filter_rel_parallel_100k
from aggregate_date_filter_rel_queries import agg_date_filter_rel, agg_date_filter_rel_parallel_100k
from aggregate_date_rel_queries import agg_date_rel, agg_date_rel_parallel_100k
import matplotlib.pyplot as plt


neo4j_username = 'neo4j'
neo4j_password = 'neo4j'
neo4j_url = "bolt://localhost:7687"

tests = 100

driver = GraphDatabase.driver(
    neo4j_url, auth=(neo4j_username, neo4j_password))
session = driver.session()


def get_avg(array):
    return sum(array) / float(len(array))


def print_load_time(query, tests):
    # Get load times
    load_times = []
    for i in range(tests):
        res = session.run(query)
        load_times.append(list(res)[0]['loadMillis'])
    # Take only the best 50% of results
    array = sorted(load_times)[:int(tests/2)]
    # Print
    print('-------------------------------------------')
    print('query: {}'.format(query))
    print('load times:{}'.format(array))
    print('Average load time is {} ms'.format(get_avg(array)))
    return get_avg(array)


def compare_parallel(query1, query2, tests):
    normal_load_time = print_load_time(query1, tests)
    parallel_load_time = print_load_time(query2, tests)

    plt.bar([0, 1], [normal_load_time, parallel_load_time],
            align='center', alpha=0.5)
    plt.xticks([0, 1], ['normal', 'parallel'])
    plt.ylabel('Average load time in ms')
    plt.title('Mode')
    plt.show()


def main():
    # Single rel
    compare_parallel(single_rel, single_rel_parallel_100k, tests)
    # Aggregate rel
    compare_parallel(agg_rel, agg_rel_parallel_100k, tests)
    # Aggregate and link sentiment filter rel
    compare_parallel(agg_filter_rel, agg_filter_rel_parallel_100k, tests)
    # Aggregate and date rel
    compare_parallel(agg_date_rel, agg_date_rel_parallel_100k, tests)
    # Aggregate and date filter + link_sentiment filter rel
    compare_parallel(agg_date_filter_rel,
                     agg_date_filter_rel_parallel_100k, tests)


if __name__ == "__main__":
    main()
