# DPLL-SAT-Solver
## CNF Encoding
The Interim Report explains how the CNF encoding was done for 15 formulas provided for Einstein Puzzle.

## SAT solver
DPLL algorithm was used to solve the puzzle using maximum weights(Jersolow Wang 2) as heuristic. The code first parses the dimacs file from CNF to clauses, which are passed on to the solver where unit propogation and the heuristic are used to backtrack and solve. 

To run the program
```
python sat_dpll.py --input_file einstein.cnf
```
