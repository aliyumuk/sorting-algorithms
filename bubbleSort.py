
def bubbleSort(items):
    length = len(items)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if items[j] > items[j+1]:
                a = items[j]
                items[j] = items[j+1]
                items[j+1] = a
    return items

list1 = [-5, -50, 8, 40, 3, 0.6, 0.5, 54, 98, 32]
list2 = ["ali", "nisa", "ayse", "melek", "nuri"]

print(bubbleSort(list1))
print(bubbleSort(list2))
