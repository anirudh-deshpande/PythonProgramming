import time

def is_palindromic_permutation(s: str) -> bool:

    chars_hash = 0

    for char in s:
        char_hash = ord(char) - ord('a')
        chars_hash ^= 1 << char_hash

    return chars_hash == 0 or (chars_hash & (chars_hash - 1)) == 0


def is_palindrome_1(s: str) -> bool:
    low, high = 0, len(s)-1

    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1

    return True


def is_palindrome_2(s:str) -> bool:
    return all(s[i] == s[~i] for i in range(len(s) // 2))



if __name__ == "__main__":
    # strs = ["abccba", "abc", "a", "b", "abcdcba", "bandnab", "abracadabra", "abradabra"]

    # for s in strs:
    #     print(s, str(is_palindromic_permutation(s)))

    for s in strs:
        start_time = time.time()
        print(str(is_palindrome_1(s)))
        print("is_palindrome_1: %s seconds", (time.time() - start_time) * 1000)

        start_time = time.time()
        print(str(is_palindrome_2(s)))
        print("is_palindrome_2: %s seconds", (time.time() - start_time) * 1000)