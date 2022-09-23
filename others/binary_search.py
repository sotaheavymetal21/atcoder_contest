# binary_search.py
def binary_search(sequence, target):
    length = len(sequence)
    low = 0
    high = length - 1
    while low <= high:
        middle = int((low + high) / 2)
        if target == sequence[middle]:
            return middle
        elif target < sequence[middle]:
            high = middle - 1
        elif target > sequence[middle]:
            low = middle + 1
    return None


seq = [1, 3, 4, 8, 13, 14, 18, 20, 21, 25]
target = 8
result = binary_search(seq, target)
if result:
    print("{} at position: {}.".format(target, result))
else:
    print('{} not in sequence.'.format(target))
