#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    string = "{} {} {} = {}\n"
    
    result = (
        string.format(a, "+", b, add(a, b)) +
        string.format(a, "-", b, sub(a, b)) +
        string.format(a, "*", b, mul(a, b)) +
        string.format(a, "/", b, div(a, b))
    )
    print(result, end="")

