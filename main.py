from unittest import result
from sympy import epath, true
import CFG.get_grammar as get_g
import CFG.grammar_convertor as gm_convert
import CFG.first_follow as ff
from CFG.ll1_parsing import ll1_parse
import CFG.m_table as mtable

while(True):
    grammar_str = get_g.get_grammar()

    print("__________________________________")
    print("Your Grammar :")
    print(grammar_str)
    
    verify = input("Is it Correct? [(y)es / (n)o]")
    
    if (verify == 'y' or verify == 'yes') :
        break
    
    
print("__________________________________")
print("Converting Grammar :")
grammar = gm_convert.convert_grammar(grammar_str)
for v, p in grammar.items():
    print("%s : %s"%(v,p))
print("__________________________________")
print("First : ")
first = ff.get_first(grammar)
print("__________________________________")
print("Follows :")
follow = ff.get_follow(grammar)


m_table = mtable.create_m_table(grammar, first, follow)

print("__________________________________")
print("M Table :")
mtable.print_m_table_2(m_table)
#print(m_table)
# S -> b A S' | d B S'
# S' -> a S" | ep
# S" -> b A S' S' | d B S' S' 
# A -> d | c c A 
# B -> d | ep
# end


# S -> b A S' | d B S'
# S' -> a S S' | ep 
# A -> d | c c A
# B -> d | ep


# S -> ) A ) | B D
# A -> B E | d A 
# B -> a B | ep
# D -> ( B ) | E b
# E -> e E | ep
# end

# E -> T E'
# E' -> + T E' | ep
# T -> F T'
# T' -> * F T' | ep
# F -> ( E ) | d
# end

while(true):
    print("_____________________________________")
    print("Enter your string for checking :")
    input_str = input('str :')
    
    if input_str == 'end':
        break
    
    reslt = ll1_parse(m_table, input_str)

    if reslt:
        print(f"The string '{input_str}' was successfully parsed.")
    else:
        print(f"The string '{input_str}' could not be parsed.")