def merge_dicts(*dict_args) -> dict:
    """
    Given any number of dictionaries, shallow copy and merge into a new dict,
    precedence goes to key-value pairs in latter dictionaries.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def union_lists(list_a: list, list_b: list) -> list:
    """
    Given two lists, union them into a new list.
    :param list_a: First list
    :type list_a: list
    :param list_b: Second list
    :type list_b: list
    :return: The united list
    """
    return list(set(list_a) | set(list_b))


def intersection(lst1: list, lst2: list) -> list:
    """
    Given two lists, intersection them into a new list.
    :param lst1: First list
    :type lst1: list
    :param lst2: Second list
    :type lst2: list
    :return: The intersection of the two lists
    """
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
