import random


def generate_random_list() -> list:
    return [random.randint(1, 100) for _ in range(10)]


def get_even_numbers(numbers) -> list:
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def get_common_numbers(list1, list2) -> set:
    return set(list1 + list2)


def is_even_or_odd(number) -> str:
    if number % 2 == 0:
        return 'even'
    return 'odd'


if __name__ == '__main__':
    random_numbers = generate_random_list()
    print(get_even_numbers(random_numbers))
    print(f'{random_numbers[0]}: {is_even_or_odd(random_numbers[0])}')
    random_list1 = generate_random_list()
    random_list2 = generate_random_list()
    print(get_common_numbers(random_list1, random_list2))
