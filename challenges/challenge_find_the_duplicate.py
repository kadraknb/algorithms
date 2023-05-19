def find_duplicate(nums):

    if len(nums) < 2 or type(nums) != list:
        return False

    counter = dict()
    for num in nums:
        if not type(num) == int or num < 0:
            return False
        if num not in counter:
            counter[num] = 1
        else:
            return num
    return False


# print(find_duplicate([1, 3, 4, 2, 2]))