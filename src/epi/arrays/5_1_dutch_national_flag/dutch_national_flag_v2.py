from typing import List


def dutch_national_flag_var2(A: List[int] , keys:List[int]) -> None:
    key_1, key_2, key_3, key_4 = keys

    next = group_keys(A, 0, key_1)
    next = group_keys(A, next, key_2)
    next = group_keys(A, next, key_3)
    group_keys(A, next, key_4)


def group_keys(A: List[int], key_index: int, key: int):
    for i in range(key_index, len(A)):
        if A[i] == key:
            A[key_index], A[i] = A[i], A[key_index]
            key_index += 1
    return key_index


if __name__ == "__main__":
    A = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
    keys = [1,2,3,4]

    dutch_national_flag_var2(A, keys)
    print(A)
