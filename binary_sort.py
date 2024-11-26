import sys


def bin_search(target, collection) -> bool:
    # initialize initial i.e first and final i.e last variables
    first = 0
    last = len(collection)
    # Base rule
    if last == 1:
        return collection[0] == target
    # find the mid-point of the collection
    middle = (first + last) // 2

    if collection[middle] == target:
        return True
    elif collection[middle] > target:
        # recall yourself
        return bin_search(target, collection[first:middle])
    elif collection[middle] < target:
        # recall yourself
        return bin_search(target, collection[middle+1:])
    else:return False

collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def get_input() -> int:
    try:
        target = int(input("Enter the search term here: "))
    except ValueError as e:
        raise ValueError(f"invalid value (must be an integer)")
    return target


print(bin_search(get_input(), collection))