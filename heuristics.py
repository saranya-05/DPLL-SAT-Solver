import random 
from collections import defaultdict

def random_choice(cnf):
    unassigned_literals = [literal for clause in cnf for literal in clause]
    if not unassigned_literals:
        return None
    return random.choice(unassigned_literals)

def two_clause(cnf):
    literal_count = {}
    for clause in cnf:
        for literal in clause:
            if literal in literal_count:
                literal_count[literal] += 1
            else:
                literal_count[literal] = 1
    two_clause_literals = [literal for literal, count in literal_count.items() if count == 2]
    if not two_clause_literals:
        return random.choice(cnf[0]) if cnf else None
    return random.choice(two_clause_literals)

def find_max_literal_weight(cnf):
    literal_weight = defaultdict(int)
    for clause in cnf:
        for literal in clause:
            literal_weight[abs(literal)] += 2 ** -len(clause)
    return max(literal_weight, key=literal_weight.get)