from neo4j import GraphDatabase


def neo4j_query(cypher_query_path):
    with open(cypher_query_path) as cypher_query_file:
        cypher_query = cypher_query_file.read()

    uri = "bolt://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "test"))

    predicate_types = set()
    predicates = []
    evidence = []
    with driver.session() as session:
        results = session.run(cypher_query)
        for record in results:
            for relationship in record:
                start_node = session.run('MATCH (n) WHERE id(n) = {id} RETURN n', id=relationship.start_node.id).single().value()
                end_node = session.run('MATCH (n) WHERE id(n) = {id} RETURN n', id=relationship.end_node.id).single().value()
                if relationship.type not in predicate_types:
                    predicate_types.add(relationship.type)
                    predicates.append({
                        'type': relationship.type,
                        'node_types': [
                            list(start_node.labels)[0],
                            list(end_node.labels)[0]
                        ]
                    })
                evidence.append({
                    'type': relationship.type,
                    'elements': [
                        start_node,
                        end_node
                    ]
                })

    return evidence, predicates
