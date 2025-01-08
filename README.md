# Expression Generator

This Python program attempts to find a mathematical expression using a set of numbers and operators that evaluates to a specific target result (2025 in this case). It generates all possible expressions by permuting the numbers and applying the operators between them.

## Features

- Uses recursion to generate all possible expressions by combining numbers with operators.
- Handles common mathematical operators: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and exponentiation (`**`).
- Handles cases like division by zero and invalid exponentiation (e.g., negative bases with fractional exponents).

## Requirements

- Python 3.x

## How it works

1. **apply_operation**: This function handles mathematical operations (`+`, `-`, `*`, `/`, `**`). It checks for division by zero and invalid exponentiation before performing the operation.
2. **generate_expressions**: This function recursively generates all possible expressions by combining numbers and applying operators. It generates every possible valid expression from permutations of the input numbers.
3. **find_solution**: This function searches through all permutations of the numbers and their generated expressions to check if any of them result in the target value (2025).
4. **Main Logic**: The main function runs the search for a solution and outputs the result if found, otherwise, it prints that no solution was found.

## Example Usage

Simply run the program:

```bash
python calculate.py
```

## Output


Generated Expression: (1 \* ((5 \*\* 2) \*(3 \*\* 4))) = 2025

