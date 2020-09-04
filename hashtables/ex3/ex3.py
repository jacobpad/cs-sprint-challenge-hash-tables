def intersection(arrays):
    """
    1. Make webster
    2. Expects a list to be returned, so make that too.
    3. Start adding values of the array to webster with associated keys that
        can be incramented (if not in webster, add it --- if already in 
        webster +1 it).
    4. For loop for webster, if value found in array 1 is also in every other array, it gets appended to result & returned.
    6. Make it work.
    """

    # Define
    webster = {}
    result = []

    # Populate Hash/dict
    for array in arrays:
        for index in array:
            if index not in webster:
                webster[index] = 1
            else:
                webster[index] += 1

    # Append fitting results
    for i in webster:
        if webster[i] > 1:
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
