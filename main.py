import random


def generate_random_list() -> list:
    return [random.randint(1, 100) for _ in range(10)]


def sum_numbers(numbers) -> int:
    return sum(numbers)


def get_unique_numbers(list1, list2) -> set:
    return set(list1) ^ set(list2)  # Симметрическая разность множеств


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    random_numbers = generate_random_list()
    print(f'Is {random_numbers[0]} prime? {is_prime(random_numbers[0])}')
    print(f'The sum of list:\n{random_numbers}\nis: {sum_numbers(random_numbers)}')
