# MLNgenerator

To run the code, install everything in requirements.txt.

Then, run the following code on a terminal:

```shell script
python main.py neo4j_query.cql mln_formulas.mln output
```

This will execute the query on neo4j_query.cql, obtain all relationships present 
in the response from the database, extract all the different predicates, and save 
everything in two lists.

Then, the results are merged with the contents of mln_formulas.mln to generate two files:
output.db and output.mln. The first one contains all the evidence from the KG,
while the second is the definition of the MLN program.

Example files to run the code are query_test.cql, formulas.mln.