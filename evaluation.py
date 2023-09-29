import os
import random
import time
from sat_dpll import dpll_eval,dpll_calls

# DPLL Solver (Implement your solvers here)

def is_satisfiable(cnf):
    # Implement your DPLL solver logic here
    pass

# Generate Random 3-SAT Instances

def generate_random_3sat(N, L):
    clauses = []
    for _ in range(L):
        clause = []
        while len(clause) < 3:
            literal = random.randint(1, N)
            if random.random() < 0.5:
                literal = -literal
            if literal not in clause:
                clause.append(literal)
        clauses.append(clause)
    return clauses

# Performance Evaluation

def evaluate_solver(N, L, num_experiments,h):
    
    satisfiable_count = 0
    total_time = 0
    for _ in range(num_experiments):
        # Generate a random 3-SAT instance
        cnf = generate_random_3sat(N, L)
        # Measure execution time
        start_time = time.time()
        satisfiable = dpll_eval(cnf,h)
        end_time = time.time()

        total_time += end_time - start_time

        # Count satisfiable instances
        if satisfiable:
            satisfiable_count += 1

    # Calculate probability of satisfiability
    satisfiability_probability = satisfiable_count / num_experiments

    # Calculate median execution time
    median_execution_time = total_time / num_experiments

    return satisfiability_probability, median_execution_time

# Main Evaluation Loop

if __name__ == '__main__':
    # Define parameters
    N_values = [100,150, 200]  # Vary the number of variables
    L_N_ratios = [3.0, 3.2, 3.4, 3.6,3.8,4.0,4.2,4.4,4.6,4.8,5.0,5.2,5.4,5.6,5.8,6.0]  # Vary the L/N ratio
    num_experiments = 100  # Number of experiments per combination
    print("Enter heuristic: 1.random-choice, 2.2-clause, 2.max-literal-weight")
    h=int(input())

    for N in N_values:
        for L_N_ratio in L_N_ratios:
            # Calculate the number of clauses (L) based on the L/N ratio
            L = int(N * L_N_ratio)

            # Perform the evaluation
            satisfiability_probability, median_execution_time = evaluate_solver(N, L, num_experiments,h)

            # Print results
            print(f"N={N}, L/N={L_N_ratio:.2f}, L={L}:")
            print(f"Probability of Satisfiability: {satisfiability_probability:.2f}")
            print(f"Median Execution Time: {median_execution_time:.4f} seconds\n")
            print(f"Number of DPLL Calls: {dpll_calls}\n")