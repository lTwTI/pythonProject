from math import sqrt


def find_square_root(value: float) -> None:
    try:
        result = sqrt(value)
    except ValueError:
        if value < -1:
            result = f'{abs(value)}i'
        else:
            result = 'i'
    print(result)
