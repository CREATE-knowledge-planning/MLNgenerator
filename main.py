import argparse

import query_parser


def write_mln_evidence(evidence, output_path):
    with open(output_path + '.db', 'w') as evidence_file:
        for evidence_piece in evidence:
            uid_start_node = '{}{}'.format(
                list(evidence_piece['elements'][0].labels)[0],
                evidence_piece['elements'][0].id
            )
            uid_end_node = '{}{}'.format(
                list(evidence_piece['elements'][1].labels)[0],
                evidence_piece['elements'][1].id
            )
            evidence_str = "{}({},{})\n".format(
                evidence_piece['type'],
                uid_start_node,
                uid_end_node
            )
            evidence_file.write(evidence_str)


def write_mln_program(predicates, formulas_path, output_path):
    with open(output_path + '.mln', 'w') as program_file:
        program_file.write('// predicate declarations\n')
        for predicate in predicates:
            predicate_str = '{}({},{})\n'.format(
                predicate['type'],
                predicate['node_types'][0],
                predicate['node_types'][1]
            )
            program_file.write(predicate_str)
        program_file.write('\n// formulas\n')
        with open(formulas_path) as formulas_file:
            program_file.write(formulas_file.read())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cypher_query", help="File with a cypher query to turn into an MLN program")
    parser.add_argument("mln_formulas", help="File with formulas that will be added to the generated MLN program")
    parser.add_argument("mln_output", help="Where to save the produced MLN evidence and program")
    args = parser.parse_args()

    evidence, predicates = query_parser.neo4j_query(args.cypher_query)
    write_mln_evidence(evidence, args.mln_output)
    write_mln_program(predicates, args.mln_formulas, args.mln_output)


if __name__ == "__main__":
    main()
