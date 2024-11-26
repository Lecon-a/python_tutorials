names = ["Sunday", "Peter", "Afolabi"]


def find_name(key, collection):
    return True if key in collection else False


def swap(collection):
    temp = collection[0]
    collection[0] = collection[-1]
    collection[-1] = temp
    return collection


print("Previous arrangement: ", names)
print("Swapped list: ", swap(names))
user_input = input("Enter the name you want to find: ")


if find_name(user_input, names):
    print("The element exists")
else:
    print("The element does not exist")
