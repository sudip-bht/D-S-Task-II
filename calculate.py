import itertools

TARGET_RESULT = 2025
NUMBERS = [1, 2, 3, 4, 5]
OPERATORS = ["+", "-", "*", "/", "**"]

def apply_operation(a, b, operator):
    """
    Safely applies a mathematical operation between two operands.

    Arguments:
    a -- The first operand (numeric value).
    b -- The second operand (numeric value).
    operator -- The operator to apply (one of '+', '-', '*', '/', '**').

    Returns:
    The result of the operation if valid; None if the operation is invalid (e.g. division by zero, invalid exponentiation).
    """
    try:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if abs(b) < 1e-12:  # division by zero
                return None
            return a / b
        elif operator == '**':
            if a < 0 and abs(b - int(b)) > 1e-12:  # negative bases with fractional exponents
                return None
            return a ** b
    except:
        return None

def generate_expressions(numbers):
    """
    Recursively generates all possible expressions by combining numbers with operators.

    Arguments:
    numbers -- A list of tuples where each tuple contains a numeric value and its string representation.

    Returns:
    A list of tuples containing the result of an operation and its corresponding string representation.
    """
    expressions = []
    if len(numbers) == 1:
        return [(numbers[0][0], numbers[0][1])]
    else:
        for i in range(1, len(numbers)):
            left_part = numbers[:i]
            right_part = numbers[i:]

            # Generate expressions for left and right parts recursively
            left_expressions = generate_expressions(left_part)
            right_expressions = generate_expressions(right_part)
            
            for valLeft, exprLeft in left_expressions:
                for valRight, exprRight in right_expressions:
                    for operator in OPERATORS:
                        result = apply_operation(valLeft, valRight, operator)
                        if result is not None:
                            expressions.append((result, f"({exprLeft} {operator} {exprRight})"))

                        # Consider reversed operations for non-commutative operators like '-', '/', '**'
                        if operator in ['-', '/', '**']:
                            result_reversed = apply_operation(valRight, valLeft, operator)
                            if result_reversed is not None:
                                expressions.append((result_reversed, f"({exprRight} {operator} {exprLeft})"))
    return expressions

def find_solution():
    """
    Searches for a valid expression that evaluates to the target result (2025).
    """
    for perm in itertools.permutations(NUMBERS):
        initial = [(float(x), str(x)) for x in perm]

        # Generate all possible expressions for the current permutation
        expressions = generate_expressions(initial)
        for value, expression in expressions:
            if abs(value - TARGET_RESULT) < 1e-9:
                return value, expression

    return None, None

def main():
    """
    The main function that calls the search function and prints the result.
    It displays the solution if found or a message stating no solution was found.
    """
    value, expression = find_solution()
    if value is not None:
        print(f"Generated Expression: {expression} = {int(value)}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
