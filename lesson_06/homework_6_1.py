string = input("Enter the string: ")
list_of_elements = list(string)
set_of_elements = set(list_of_elements)
print(set_of_elements)
count = sum(1 for element in set_of_elements if list_of_elements.count(element) == 1)

if count > 10:
    print(True)
else:
    print(False)

