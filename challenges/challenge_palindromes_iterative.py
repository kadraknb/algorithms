def is_palindrome_iterative(word):

    if len(word) == 0:
        return False

    word_lower = word.lower()
    low_index = 0
    high_index = len(word) - 1

    for _ in range(len(word)):
        if word_lower[low_index] != word_lower[high_index]:
            return False
        low_index += 1
        high_index -= 1

    return True
