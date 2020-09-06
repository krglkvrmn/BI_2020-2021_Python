from math import floor


while True:
    try:
        a = float(input())
        operator = input()
        assert operator in ('+', '-', '/', '*', '**', '//', '%')
        b = float(input())
        expression = f'{a}{operator}{b}'
        float_res = eval(expression)
        # Return integer value if possible. For example: 5.0 -> 5
        result = int(float_res) if floor(float_res) == float_res else float_res

    # Start again if invalid operator is entered.
    except AssertionError:
        print('Invalid operator. Try again.')
        continue
    # Start again if division by zero was performed.
    except ZeroDivisionError:
        print('Zero division! Try again.')
        continue
    # Start again if operands are not numbers.
    except ValueError:
        print('Operands must be numbers. Try again.')
        continue
    print(result)
