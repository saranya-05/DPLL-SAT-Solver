import random 
from collections import defaultdict

def random_choice(cnf):
    unassigned_literals = [literal for clause in cnf for literal in clause]
    
    if not unassigned_literals:
        return None
    
    return random.choice(unassigned_literals)

'''def random_choice(cnf):
    unassigned_literals = [literal for clause in cnf for literal in clause if -literal not in clause]
    return random.choice(unassigned_literals)'''

def two_clause(cnf):
    # Count the occurrences of each literal in remaining clauses
    literal_count = {}
    for clause in cnf:
        for literal in clause:
            if literal in literal_count:
                literal_count[literal] += 1
            else:
                literal_count[literal] = 1

    # Filter literals that appear in exactly two clauses
    two_clause_literals = [literal for literal, count in literal_count.items() if count == 2]

    if not two_clause_literals:
        # No literals appear in exactly two clauses, return a random choice
        return random.choice(cnf[0]) if cnf else None

    # Select a literal from those that appear in exactly two clauses
    return random.choice(two_clause_literals)

'''def two_clause(cnf):
    literal_count = defaultdict(int)
    for clause in cnf:
        if len(clause) == 2:
            for literal in clause:
                literal_count[abs(literal)] += 1
    selected_literal = max(literal_count, key=literal_count.get)
    return selected_literal'''

def find_max_literal_weight(cnf):
    literal_weight = defaultdict(int)
    for clause in cnf:
        for literal in clause:
            literal_weight[abs(literal)] += 2 ** -len(clause)
    return max(literal_weight, key=literal_weight.get)

def most_occurrences_heuristic(cnf):
    literal_count = defaultdict(int)
    for clause in cnf:
        for literal in clause:
            literal_count[abs(literal)] += 1
    selected_literal = max(literal_count, key=literal_count.get)
    return selected_literal