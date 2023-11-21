import CFG.get_grammar as get_g
import CFG.grammar_convertor as gm_convert
import CFG.first_follow as ff

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
print(grammar)
print("__________________________________")
print("First : ")
first = ff.get_first(grammar)
print("__________________________________")
print("Follows :")
follow = ff.get_follow(grammar)