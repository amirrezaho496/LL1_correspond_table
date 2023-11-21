def convert_grammar(grammar_str):
    grammar = {}
    rules = grammar_str.split('\n')
    for rule in rules:
        if '->' not in rule:
            print(f"Skipping invalid rule: {rule}")
            continue
        lhs, rhs = rule.split('->')
        lhs = lhs.strip()
        rhs = [prod.split() for prod in rhs.split('|')]
        grammar[lhs] = rhs
    return grammar

# Your grammar as a string
# grammar_str = """
# S -> a B b | ab | a
# B -> a | aaa | bb | ab C c
# C -> a | c | ac | aaaaa | S
# """

# Convert the string to a dictionary
# grammar_dict = convert_grammar(grammar_str)
# print(grammar_dict)
