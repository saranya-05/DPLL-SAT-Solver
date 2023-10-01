# DPLL-SAT-Solver
## CNF Encoding
The Interim Report explains how the CNF encoding was done for 15 formulas provided for Einstein Puzzle.

## SAT solver
DPLL algorithm was used to solve the puzzle using maximum weights(Jersolow Wang 2) as heuristic. The code first parses the dimacs file from CNF to clauses, which are passed on to the solver where unit propogation and the heuristic are used to backtrack and solve. 

To run the program
```
python3 sat_dpll.py

```

## Heuristics
Random-choice, 2-Clause, and Max-Literal-Weight were implemented in heuristics.py

## Evaluation
The performance of the 3 heuristics was evaluated using its computation time for different sizes of CNF in evaluation.py

To run the evaluation
```
python3 evaluation.py

```


