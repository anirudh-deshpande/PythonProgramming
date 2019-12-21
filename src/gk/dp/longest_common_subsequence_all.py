import time
import sys


def longest_common_subsequence(s1, s2, i, j, count):
    """
    Running time: 1 hour, and was still running
    Space: O(max(m,n)) for stack space at a time
    """

    if i >= len(s1) or j >= len(s2):
        return count

    if s1[i] == s2[j]:
        count = 1 + longest_common_subsequence(s1, s2, i+1, j+1, count)
    else:
        count = max(longest_common_subsequence(s1, s2, i, j+1, count),
                    longest_common_subsequence(s1, s2, i+1, j, count))

    return count


def longest_common_subsequence_with_memo(s1, s2, i, j, count, cache):
    """
    Running time = O(m*n), as parameters i & j together vary m*n times
    Space: O(m*n) for cache

    Running time: 0.555317sec
    """

    # print('s1[', i, ']', 's2[', j, ']')
    if i >= len(s1) or j >= len(s2):
        return 0 # bug

    if cache[i][j] != -1:
        return cache[i][j]

    if s1[i] == s2[j]:
        count = 1 + longest_common_subsequence_with_memo(s1, s2, i + 1, j + 1, count, cache)
    else:
        count = max(longest_common_subsequence_with_memo(s1, s2, i, j + 1, count, cache),
                    longest_common_subsequence_with_memo(s1, s2, i + 1, j, count, cache))

    cache[i][j] = count
    return cache[i][j]


def longest_common_subsequence_with_iteration(s1, s2):
    """
    Build from bottom up, referring above algorithm
    Running time = O(m*n), as parameters i & j together vary m*n times
    Space: O(m*n) for cache

    Running time: 0.36252799999999996 secs
    """
    cache = [[0] * (len(s2)+1) for _ in range(-1, len(s1))]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):

            if s1[i-1] == s2[j-1]:
                cache[i][j] = cache[i-1][j-1] + 1

            else:
                cache[i][j] = max(cache[i][j-1], cache[i-1][j])

    return cache[-1][-1]


def longest_common_subsequence_with_iteration_memory_opt(s1, s2):
    """
    Use just 2 arrays instead of 2D cache
    Running time = O(m*n), as parameters i & j together vary m*n times
    Space: O(n) for prev and cur

    Running time: 0.2980760000000001 sec
    """
    prev = [0] * (len(s2)+1)
    cur = [0] * (len(s2)+1)

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):

            if s1[i-1] == s2[j-1]:
                cur[j] = prev[j-1] + 1
            else:
                cur[j] = max(cur[j-1], prev[j])

        prev = cur
        cur = [0] * (len(s2) + 1)

    return prev[-1]


if __name__ == "__main__":
    sys.setrecursionlimit(5000)

    s1 = "passportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassportpassport"
    s2 = "ppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppssptppsspt"

    # start = time.process_time()
    # print(longest_common_substring(s1, s2, 0, 0, 0))
    # print(time.process_time() - start)

    cache = [[-1] * len(s2) for _ in range(len(s1))]

    start = time.process_time()
    print(longest_common_subsequence_with_memo(s1, s2, 0, 0, 0, cache))
    print(time.process_time() - start)

    start = time.process_time()
    print(longest_common_subsequence_with_iteration(s1, s2))
    print(time.process_time() - start)

    start = time.process_time()
    print(longest_common_subsequence_with_iteration_memory_opt(s1, s2))
    print(time.process_time() - start)
