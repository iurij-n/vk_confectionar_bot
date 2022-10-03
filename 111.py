dict_list = [
    {"key1": "value1"},
    {"k1": "v1", "k2": "v2", "k3": "v3"},
    {},
    {},
    {"key1": "value1"},
    {"key1": "value1"},
    {"key2": "value2"}
]

def remove_duplicates(init_list: list) -> list:
    """
    Функция принимает список элементов и возврщает
    список уникальных элементов исходного набора значений
    """
    result_list = []
    
    [result_list.append(list_element)
        for list_element in init_list
            if list_element not in result_list]
    
    return result_list


print(remove_duplicates([1, '1', 1, 2, '2', 3, 3, 4]))

