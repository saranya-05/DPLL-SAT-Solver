from collections import defaultdict
import os
import time
import argparse
from heuristics import random_choice,two_clause,find_max_literal_weight,most_occurrences_heuristic

def parse_dimacs(file_path):
    parsed_clauses = []
    with open(file_path, 'r') as dimacs_file:
        for line in dimacs_file:
            if line.startswith('c') or line.startswith('p'):
                continue
            clause = list(map(int, line.split()[:-1]))
            parsed_clauses.append(clause)
    
    return parsed_clauses

def propagate_unit(cnf, unit):
    new_cnf = []
    for clause in cnf:
        if unit in clause:
            continue
        if -unit in clause:
            new_clause = [literal for literal in clause if literal != -unit]
            if not new_clause:
                return -1
            new_cnf.append(new_clause)
        else:
            new_cnf.append(clause)
    return new_cnf

def assign_unit(clauses):
    assigned_literals = []
    unit_clauses = [clause for clause in clauses if len(clause) == 1]
    
    while unit_clauses:
        unit_literal = unit_clauses[0][0]
        clauses = propagate_unit(clauses, unit_literal)
        assigned_literals.append(unit_literal)
        
        if clauses == -1:
            return -1, []
        
        if not clauses:
            return clauses, assigned_literals
        
        unit_clauses = [clause for clause in clauses if len(clause) == 1]
    
    return clauses, assigned_literals

def dpll(cnf, I,h):
    global dpll_calls
    dpll_calls+=1
    cnf, unit_I = assign_unit(cnf)
    I = I + unit_I
    if cnf == -1:
        return []
    if not cnf:
        return I
    
    if h==1:
        selected_literal = random_choice(cnf)
    elif h==2:
        selected_literal = two_clause(cnf)
    else:
        selected_literal = find_max_literal_weight(cnf)
    
    res = dpll(propagate_unit(cnf, selected_literal), I + [selected_literal],h)
    if not res:
        res = dpll(propagate_unit(cnf, -selected_literal), I + [-selected_literal],h)
    return res

def dpll_main():
    print("Enter heuristic: 1.random-choice, 2.2-clause, 2.max-literal-weight")
    h=int(input())
    clauses = parse_dimacs("einstein.cnf")
    assignment = dpll(clauses, [],h)
    if assignment:
        print('SAT')
        assignment.sort(key=lambda x: abs(x))
        print(assignment)
    else:
        print('UNSAT')
        

dpll_calls = 0

def dpll_eval(f,h):
    assignment = dpll(f, [],h)
    if assignment:
        return True
    else:
        return False
    
dpll_main()