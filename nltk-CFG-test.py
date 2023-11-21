from nltk import CFG, Nonterminal
from nltk.parse.generate import generate

def print_lm(grammar):
    # Parse the CFG
    cfg = CFG.fromstring(grammar)
    
    # Generate sentences from the CFG
    for sentence in generate(cfg):
        print(' '.join(sentence))

# Define your CFG here
cfg_grammar = """
  S -> 'a' B 'b' | 'ab' | 'a'
  B -> 'a' | 'aaa' | 'bb' | 'ab' C 'c'
  C -> 'a' | 'c' | 'ac' | 'aaaaa' | S
"""

print_lm(cfg_grammar)
