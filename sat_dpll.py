from collections import defaultdict
import os
import time
import argparse

def parse_dimacs(file_path):
    parsed_clauses = []
    with open(file_path, 'r') as dimacs_file:
        for line in dimacs_file:
            if line.startswith('c') or line.startswith('p'):
                continue
            clause = list(map(int, line.split()[:-1]))
            parsed_clauses.append(clause)
    
    return parsed_clauses

def find_max_literal_weight(cnf):
    literal_weight = defaultdict(int)
    for clause in cnf:
        for literal in clause:
            literal_weight[abs(literal)] += 2 ** -len(clause)
    return max(literal_weight, key=literal_weight.get)

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


def dpll(cnf, I):
    cnf, unit_I = assign_unit(cnf)
    I = I + unit_I
    if cnf == -1:
        return []
    if not cnf:
        return I
    selected_literal = find_max_literal_weight(cnf)
    res = dpll(propagate_unit(cnf, selected_literal), I + [selected_literal])
    if not res:
        res = dpll(propagate_unit(cnf, -selected_literal), I + [-selected_literal])
    return res

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', default=None)
    args = parser.parse_args()
  
    if args.input_file is not None:
        f = args.input_file
        clauses = parse_dimacs(f)
        assignment = dpll(clauses, [])
        if assignment:
            print('SAT')
            assignment.sort(key=lambda x: abs(x))
            print(assignment)
        else:
            print('UNSAT')