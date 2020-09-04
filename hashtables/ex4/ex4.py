def has_negatives(a):
    """
    - Make webster and cousin 
    - Loop over list(a) and get the absolute value
      - And get the absolute value append to result
    - Return
    """
    # Make webster and cousin
    webster = {}
    result = []

    for num in a:
        webster[num] = 1
        if num != 0 and -num in webster:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
