list_ = [1, 2, 3, 4, 5, 6]
new_set = set(list_)


def find_unique_numbers(list_, new_set):
    if len(list_) == len(new_set):
        return 'Все числа уникальны'
    else:
        return 'Есть повторяющиеся числа'


find_unique_numbers(list_, new_set)
