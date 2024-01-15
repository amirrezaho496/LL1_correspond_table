from CFG.constants import DOLLOR


EPSILON = 'ε'
def first(grammar, symbol):
    """
    Calculate the FIRST set for a given non-terminal symbol in a context-free grammar.

    Parameters:
    grammar (dict): The context-free grammar, represented as a dictionary where the keys are non-terminal symbols and the values are lists of productions.
    symbol (str): The non-terminal symbol for which to calculate the FIRST set.

    Returns:
    set: The FIRST set for the given non-terminal symbol.
    """    
    first_set = set()
    if symbol not in grammar:
        return set(symbol)
    for prod in grammar[symbol]:
        first_symbol = prod[0]
        
        if first_symbol == EPSILON:
            first_set.add(EPSILON)
            
        elif first_symbol in grammar:  # If the first symbol is a non-terminal (variable)
            for symb in prod:
                symb_firsts : set = first(grammar, symb) 
                first_set |= (symb_firsts - set(EPSILON))
                if (not symb_firsts.__contains__(EPSILON)):
                    break
                
                # If the current symbol is the last in the production and can derive EPSILON, add EPSILON to the FIRST set
                if prod[-1] == symb and symb_firsts.__contains__(EPSILON):
                    first_set.add(EPSILON)
                    break
            
        else:  # If the first symbol is a terminal
            first_set.add(first_symbol)
    return first_set
def follow(grammar, term, seen=None):
    
    # 'seen' is used to track processed non-terminals and prevent infinite recursion
    if seen is None:
        seen = set()  # Keep track of the non-terminals we've already seen
    elif term in seen:
        return set()  # If non-terminal have seen before, return an empty set to break the cycle

    seen.add(term)

    follow_set = set()
    
    # Transform the grammar into a dictionary where each production is a list of symbols
    prods = {}
    for key, valueList in grammar.items():
        prods[key] = []
        for productionRule in valueList:
            prod = []
            for productionList in productionRule:
                prod.append(productionList)
            prods[key].append(prod)
            
    if term == next(iter(grammar)):
        follow_set.add(DOLLOR)
    for key, values in prods.items():
        for value in values:
            if term in value:
                following_seq = value[value.index(term) + 1:]
                if following_seq:
                    if EPSILON in first(grammar, following_seq[0]):
                        follow_set |= (first(grammar, following_seq[0]) - set(EPSILON)) | follow(grammar, key, seen)
                    else:
                        follow_set |= first(grammar, following_seq[0])
                else:
                    follow_set |= follow(grammar, key, seen)
    return follow_set



def get_first(grammar : dict[str, list]) : 
    first_dict : dict[str, set] = {}
    for non_term in grammar:
        first_n = first(grammar, non_term)
        first_dict[non_term] = first_n
        
        print(f'FIRST({non_term}) = {first_n}')
    
    return first_dict

def get_follow(grammar : dict[str, list]) : 
    first_dict : dict[str, set] = {}
    for non_term in grammar:
        first_n = follow(grammar, non_term)
        first_dict[non_term] = first_n
        
        print(f'FOLLOW({non_term}) = {first_n}')
    
    return first_dict

# Define the grammar
# grammar = {
#     'S': [['a', 'B', 'b'], ['ab'], ['a']],
#     'B': [['a'], ['aaa'], ['bb'], ['ab', 'C', 'c']],
#     'C': [['a'], ['c'], ['ac'], ['aaaaa'], ['S']]
# }

# grammar_str = """
# S -> a B b | ab | a
# B -> a | aaa | bb | ab C c
# C -> a | c | ac | aaaaa | S
# """

# grammar = gm_convert.convert_grammar(grammar_str)

# # Calculate FIRST and FOLLOW sets
# for non_term in grammar:
#     print(f'FIRST({non_term}) = {first(grammar, non_term)}')
#     print(f'FOLLOW({non_term}) = {follow(grammar, non_term)}')

