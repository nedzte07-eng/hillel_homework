# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
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

rev_list = ReversedListIterator([1,2,3,4,5,6,7,8,9,10])

for i in rev_list:
    print(i)
print("-" * 80)

#Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
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













