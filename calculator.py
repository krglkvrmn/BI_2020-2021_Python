from math import floor


while True:
    try:
        a = float(input())
        operator = input()
        assert operator in ('+', '-', '/', '*', '**')
        b = float(input())
        expression = f'{a} {operator} {b}'
        float_res = eval(expression)
        result = int(float_res) if floor(float_res) == float_res else float_res
    except AssertionError:
        print('Invalid operator. Try again.')
        continue
    except ZeroDivisionError:
        print('Zero division! Try again.')
        continue
    except ValueError:
        print('Operands must be numbers. Try again.')
        continue
    print(result)
