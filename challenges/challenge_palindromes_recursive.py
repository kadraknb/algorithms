def is_palindrome_recursive(word, low_index, high_index):

    if len(word) == 0 or word[low_index] != word[high_index]:
        return False
    if len(word) - 1 == low_index:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
