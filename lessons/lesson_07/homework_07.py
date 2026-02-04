# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    result = 0
    while result <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            return result
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(9)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_integer(a:int, b:int) -> int:
    return a + b

print(sum_of_integer(7, 8))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_of_list(a:list) -> float:
    return sum(a) / len(a)

print(round(average_of_list([9, 15, 20]), 2))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(a:str) -> str:
    return a[::-1]

print(reverse_string("Hello, world!"))
print(reverse_string("Never odd or even"))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def the_longest_word(a:list) -> str:
    length = 0
    result_list = []
    for word in a:
        if len(word) >= length:
            length = len(word)
    for word in a:
        if len(word) == length:
            result_list.append(word)
    return ", ".join(result_list)

print(the_longest_word(["Hello", "world", "!"]))
print(the_longest_word(["Hello", "world", "!", "asdjkasdjklhjkasfhjk"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    result = str1.find(str2)
    return result

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def start_with(a:str) -> bool:
    """
    Приймає речення і повертає тру, якщо воно починається на By the time, фолс в іншому випадку
    :param a: речення
    :return: boolean
    """
    if a.startswith("By the time"):
        return True
    else:
        return False

print(start_with("The quick brown fox jumps over the lazy dog"))
print(start_with("By the time the quick brown fox jumps over the lazy dog"))


# task 8
def more_than_ten_different_symbols(a:str) -> bool:
    """
    Перевіряє чи є більше десяти різних символів в строці
    :param a: строка
    :return: правда/неправда
    """
    list_of_elements = list(a)
    set_of_elements = set(list_of_elements)
#    print(set_of_elements)
    count = sum(1 for element in set_of_elements if list_of_elements.count(element) == 1)

    if count > 10:
        return True
    else:
        return False

print(more_than_ten_different_symbols("By the time"))
print(more_than_ten_different_symbols("qwerty asdf"))

# task 9
def string_separator(a:list) -> list:
    """
    Вибирає стрінги зі списка з різними типами елементів
    :param a: вхідний список
    :return: сепарований список
    """
    lst2 = []

    for item in a:
        if type(item) is str:
            lst2.append(item)

    return lst2

print(string_separator(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']))

# task 10
def sum_of_even(a:list) -> int:
    """
    Повертає суму парних чисел зі списку
    :param a: список
    :return: сума парних чисел списка
    """
    counter_sum_of_even = 0
    for item in a:
        if item % 2 == 0:
            counter_sum_of_even += item

    return counter_sum_of_even

print(sum_of_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]))
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""