import sys
from typing import List
from convert import str_to_float

def sum_command_line_args(args: List[str]) -> float:
    total = 0.0
    for arg in args:
        number = str_to_float(arg)
        if number is not None:
            total += number
    return total

if __name__ == '__main__':
    # sys.argv[1:] skips the first element (the script name)
    result = sum_command_line_args(sys.argv[1:])
    print("Sum of command-line arguments:", result)

