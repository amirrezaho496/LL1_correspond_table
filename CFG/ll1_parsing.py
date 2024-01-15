import CFG.constants as cnts

def ll1_parse(m_table : dict[str, dict[str, list[str]]] , input_string):
    # Initialize the stack with the start symbol
    stack = ['$', list(m_table.keys())[0]]

    # Add the end-of-input marker to the input string
    input_string += '$'

    # Initialize the input pointer
    input_pointer = 0

    print(f"{'Stack':<20} | {'String':<20} | {'Productions':<20}")
    while len(stack) > 0:
        top = stack[-1]

        if top == cnts.EPSILON:
            stack.pop()
            continue
        
        if top in m_table:
            # The top of the stack is a non-terminal
            if input_string[input_pointer] in m_table[top]:
                # There is a production for the current token
                stack.pop()
                production = m_table[top][input_string[input_pointer]][top]
                # Push the symbols in the production onto the stack in reverse order
                stack.extend(production[::-1])
                var = top
            else:
                # There is no production for the current token
                return False
        else:
            # The top of the stack is a terminal
            if top == input_string[input_pointer]:
                # The terminal matches the current token
                stack.pop()
                input_pointer += 1
            else:
                # The terminal does not match the current token
                return False

        
        stack_string = " ".join(stack)
        left_string = input_string[input_pointer:]
            
        print(f"{str(stack_string):<20} | {str(left_string):<20} | {str(var)}->{str(''.join(production)):<20}")
        pass
        
    # Check if all tokens have been consumed
    if input_pointer != len(input_string):
        return False

    # The input string was successfully parsed
    return True
            

