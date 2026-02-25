# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
import logging
import inspect


def even_numbers_generator(n):
    a = 0
    while a <= n:
        yield a
        a += 2


even = even_numbers_generator(5)


# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_generator(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


def check_generator(func, r: int):
    checked = func
    for i in range(r):
        try:
            print(next(func))
        except StopIteration as stop:
            print(f'Generator raised {stop.__class__.__name__}')
            break
    print("-" * 80)


check_generator(even_numbers_generator(8), 4)

check_generator(fibonacci_generator(20), 25)


# Реалізуйте ітератор для зворотного виведення елементів списку.
class ReversedListIterator:
    def __init__(self, lst):
        self.lst = lst[::-1]
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.i += 1
            return self.lst[self.i]
        except:
            raise StopIteration


rev_list = ReversedListIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in rev_list:
    print(i)
print("-" * 80)


# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenNumbersIterator:
    def __init__(self, n):
        self.n = n
        self.num = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        if self.num > self.n:
            raise StopIteration
        return self.num


ev_nums = EvenNumbersIterator(15)

for i in ev_nums:
    print(i)
print("-" * 80)

# Напишіть декоратор, який логує аргументи та результати викликаної функції.
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


def decorator_arguments_results(func):
    def wrapper(*args):
        # print(f"Arguments are / is {args}")
        logger.info(f"Arguments are / is {args}")
        result = func(*args)
        # print(f"Result is {result}")
        logger.info(f"Result is {result}")

    return wrapper


@decorator_arguments_results
def max_of_list(n: list) -> int:
    return max(n)


maximum = max_of_list([1, 6, 4])


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def decorator_of_exceptions(func):
    def wrapper(*args):
        try:
            func(*args)
        except Exception as e:
            logger.error(f"The function is failed with {e} exception")

    return wrapper


@decorator_of_exceptions
def positive_value(n: int) -> int:
    if n > 0:
        return n
    else:
        raise TypeError("VALUE IS NEGATIVE")


positive = positive_value(10)
negative = positive_value(-10)
