def count_unique(list):
    """Count the number of distinct elements in a list.

    The list can contain any kind of elements, including duplicates and nulls in any order.

    (In PyDoc there are different formats for parameters and returns. Use what you prefer.)

    :param list:  list of elements to find distinct elements of
    :return: the number of distinct elements in list

    Examples:
    >>> count_unique(['a','b','b','b','a','c','c'])
    3
    >>> count_unique(['a','a','a','a'])
    1
    >>> count_unique([ ])
    0
    """

    list2 = []
    for i in list:
        if (i not in list2):
            list2.append(i)

    return len(list2)


count_unique(list)



def binary_search(list,element):
    left = 0
    right = len(list)-1
    element == list[element]
    [mid] = (left + right)//2
    if list[mid]<element :
         left = [mid] + 1
    elif list[mid]> element:
        right = [mid] +1
    elif list[mid] == element:
        return element
    elif left > right:
        return -1

