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

collection = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_input() -> int:
    return int(input("Enter the search term (must be an integer) here: "))

print(bin_search(get_input(), collection))