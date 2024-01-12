
def convert_grammar(grammar_str : str):
    grammar: dict[str, list[list[str]]] = {}
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
# S -> A a b | a b | ε
# A -> B | a | b
# B -> B bb | b | ε
# """

# Convert the string to a dictionary
# grammar_dict = convert_grammar(grammar_str)
# => 
# {
#   'S': [['A', 'a', 'b'], ['a', 'b'], ['ε']],
#   'A': [['B'], ['a'], ['b']], 
#   'B': [['B', 'bb'], ['b'], ['ε']]
# }
