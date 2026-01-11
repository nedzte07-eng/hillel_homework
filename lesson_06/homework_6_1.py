string = input("Enter the string: ")
list_of_elements = list(string)
count = 0
for element in list_of_elements:
  if list_of_elements.count(element) == 1:
      count = count + 1

if count > 10:
    print(True)
else:
    print(False)

