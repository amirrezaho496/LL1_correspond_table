from CFG.constants import EPSILON, INPUT_EPSILON
def get_grammar():
    grammar = ""
    print(f"Enter your grammar productions (use 'ep' for epsilon('ε') and 'end' to finish):")
    while True:
        line = input()
        if line == 'end':
            break
        grammar += line.replace(INPUT_EPSILON, EPSILON) + '\n'
    return grammar

# Get the grammar from the user
# grammar = get_grammar()
# print("Your grammar is:")
# print(grammar)
