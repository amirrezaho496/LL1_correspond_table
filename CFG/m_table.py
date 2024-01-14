import CFG.constants as cnts
def create_m_table(grammar: dict[str, list[list[str]]], all_firsts: dict, all_follows: dict):
    # Initialize m_table with all non-terminals in the grammar
    m_table = {non_terminal: {} for non_terminal in grammar.keys()}

    for non_terminal, productions in grammar.items():
        for production in productions:
            # Check if the first symbol of the production is a terminal
            if production[0] in all_firsts:
                first = set()
                for p in production:
                    # check if p is a terminal 
                    if p not in all_firsts:
                        first |= {p} 
                    else:
                        if cnts.EPSILON in all_firsts[p]:
                            first |= all_firsts[p] - {cnts.EPSILON}
                            if p == production[-1] :
                                first |= all_follows[non_terminal]
                        else :
                            first |= all_firsts[p]     
            else:
                if production[0] == cnts.EPSILON :
                    first = all_follows[non_terminal]
                else :
                    first = {production[0]}  # The First set of a terminal is the terminal itself

            # # If the First set contains 'ε', include the Follow set of the non-terminal
            # if cnts.EPSILON in first:
            #     first |= all_follows[non_terminal]
            #     first.remove(cnts.EPSILON)  # Remove cnts.EPSILON from the First set

            for terminal in first:
                if terminal not in m_table[non_terminal]:
                    m_table[non_terminal][terminal] = {}
                m_table[non_terminal][terminal][non_terminal]=production

            # if cnts.EPSILON in first:
            #     for terminal in all_follows[non_terminal]:
            #         if terminal not in m_table[non_terminal]:
            #             m_table[non_terminal][terminal] = {}
            #         m_table[non_terminal][terminal][non_terminal]=production

    return m_table


def print_m_table(m_table: dict[str, dict[str, list[str]]]) -> None:
    for non_terminal, terminals in m_table.items():
        print(f"{non_terminal} : ")
        for terminal, productions in terminals.items():
            print(f"\t{terminal} : {productions}")


def print_m_table_2(m_table: dict[str, dict[str, list[str]]]) -> None:
    # Get all terminals in the M-table
    all_terminals = set(terminal for terminals in m_table.values() for terminal in terminals.keys())

    # Print the header row with an initial empty space for alignment
    print(f"{'var':<8}" + "\t".join([f"{terminal:<20}" for terminal in all_terminals]))

    for non_terminal in m_table:
        row = [non_terminal]
        for terminal in all_terminals:
            if terminal in m_table[non_terminal]:
                # Convert the production list to a string and prepend the non-terminal
                production_str = non_terminal + " -> " + " ".join(m_table[non_terminal][terminal][non_terminal])
                row.append(f"{production_str:<20}")
            else:
                row.append("error" + " " * 15)  # Fill up the remaining space with spaces
        # Print the row
        print("\t".join(row))


