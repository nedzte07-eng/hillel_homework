example = ["1,2,3,4", "1,2,   3,4, 50   ", "qwerty1,2,3", "0,  0,0  ,0", "-5"]

def totals_of_iists_items (data_list):
    result = []
    for i in example:

        i = i.strip()
        splited_list = i.split(',')
        total = 0
        for j in splited_list:
            try:
                j = j.strip()
                total += int(j)
            except ValueError as e:
                print(f"Неправильні дані, виникла помилка {e}")
                total = 'failure'
                break
        if total == 'failure':
            continue
        print(total)
        result.append(total)
    return result

print(totals_of_iists_items(example))

