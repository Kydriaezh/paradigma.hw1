# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
def sort_list_declarative(numbers):
    return sorted(numbers, key=lambda x: -x);


print(sort_list_declarative([3, 7, 1, 4, 8]))
