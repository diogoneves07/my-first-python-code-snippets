"""
    Simple exemple of Fibonacci sequence.
        Functions:
            fibonacci(limit:int) -> None
            get_user_value() -> None
"""


def fibonacci(limit: int = 1):
    """
    Fibonacci sequence.

        Args:
            limit (int, optional): The number limit to avoid infinite loop. Defaults to 1.
    """
    current_value, next_value = 0, 1
    fib_sequence = []
    while current_value < limit:
        fib_sequence.append(current_value)
        current_value, next_value = next_value, current_value+next_value
    print(f'\n{fib_sequence}\n')


def get_user_value():
    """ Gets a number from user and cauculates your Fibonacci sequence."""

    user_input = input(
        "\nInsert a number to get your Fibonacci sequence or 'q' to finish this program: ")

    if user_input.strip() == 'q':
        print("\nTake care, see yoo soon!\n")
        return
    try:

        user_value = int(user_input)
        fibonacci(user_value)

    except ValueError:
        print("\n\nPlease, insert a integer number!!!")
    get_user_value()


get_user_value()
