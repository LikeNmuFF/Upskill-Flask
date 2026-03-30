"""Quick-reference notes: basic Python functions, parameters, *args, **kwargs,
and simple control flow.

Run this file directly to see printed examples for each concept.
"""


def greet():
    """Print a fixed, no-argument greeting.

    Use when you just want to execute the function body without inputs.
    """

    print("Hi Klein Ric")
    print("Welcome Aboard!")


# Demonstration: calling a zero-parameter function
greet()


def greets(first_name, last_name):
    """Show how positional parameters work.

    Parameters
    ----------
    first_name : str
        First name supplied by the caller.
    last_name : str
        Last name supplied by the caller.
    """

    print(f"Hi {first_name} {last_name}")
    print("Welcome Aboard")


# Demonstration: two positional arguments map onto the two parameters above
greets("Klein", "Ric")
greets("Erica", "Joy")


def multiply(*numbers):
    """Multiply an arbitrary count of numbers and return the product.

    *numbers collects any extra positional arguments into a tuple. This is
    useful when you do not know how many values the caller will pass.
    """

    result = 1
    for value in numbers:  # iterate through the collected tuple
        result *= value    # accumulate the product
    return result


# Demonstration: passing 4 numbers; you could pass any count (including 0)
print(multiply(2, 3, 4, 5))


def info(**user):
    """Capture keyword arguments into a dictionary and print them.

    **user gathers named arguments (key=value pairs) into a dict. This pattern
    is handy for optional or open-ended metadata where keys are not fixed.
    """

    print(user)


# Demonstration: building a dict from keyword arguments
info(id=2, name="klein", age=21)


def fizz_buzz(value):
    """Classic FizzBuzz using conditional branches.

    Prints:
    - 'fizzbuzz' if divisible by both 3 and 5
    - 'buzz' if only divisible by 5
    - 'fizz' if only divisible by 3
    - the original number otherwise
    """

    if value % 3 == 0 and value % 5 == 0:  # divisible by 3 and 5
        print("fizzbuzz")
    elif value % 5 == 0:                   # divisible by 5 only
        print("buzz")
    elif value % 3 == 0:                   # divisible by 3 only
        print("fizz")
    else:                                  # not divisible by 3 or 5
        print(value)


# Demonstration: run fizz_buzz on a single sample value
fizz_buzz(7)
