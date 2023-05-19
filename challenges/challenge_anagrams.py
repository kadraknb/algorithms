def sort(string):
    string = string.lower()
    if len(string) <= 1:
        return string
    pivot = string[0]
    smaller = ''.join(x for x in string[1:] if x < pivot)
    equal = ''.join(x for x in string if x == pivot)
    larger = ''.join(x for x in string[1:] if x > pivot)
    return sort(smaller) + equal + sort(larger)


def is_anagram(first_string, second_string):

    first_sorted = "".join(sort(first_string))
    second_sorted = "".join(sort(second_string))

    if first_string == "" or second_string == "":
        return (first_sorted, second_sorted, False)

    for i in range(0, len(first_sorted)):
        if first_sorted[i] != second_sorted[i]:
            return (first_sorted, second_sorted, False)
    return (first_sorted, second_sorted, True)
