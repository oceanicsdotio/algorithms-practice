def reverse_string(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("Not a string")
    length = len(string)
    if length < 2:
        return string  # save some cycles, and avoid empty string error condition
    rev = ""
    for ind in range(-1, -(length+1), -1):
        rev += string[ind]
    return rev


def is_palindrome(string: str) -> bool:
    if not isinstance(string, str):
        raise TypeError("Not a string, could still be a palindrome")
    length = len(string)
    if not length:
        raise ValueError("Debate-able whether an empty string is a palidrome, but let's say not")

    for ind in range(0, length // 2):
        if string[ind] != string[-(ind+1)]:
            return False

    return True


def are_anagrams(strings: (str, str)) -> bool:

    if not isinstance(strings, (tuple, list)) or not all(map(lambda x: isinstance(x, str), strings)):
        raise TypeError("Not an iterable of strings, could still be anagrams")
    
    inc = 1
    work_index = dict()
    # method only works with 2, but easier to understand than `functools.reduce` method for "all cases"
    for string in strings:
        for symbol in string.lower():  # probably should do some string normalization depending on source
            if symbol in work_index:
                work_index[symbol] += inc
            else:
                work_index[symbol] = 1
        inc *= -1
    
    return not any(work_index.values())

    
    

    
        


    