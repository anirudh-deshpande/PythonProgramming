import sys
import time

def longest_common_substring_backtrack(s1, s2, i, j, count):
    """
    Takes forever

    This is top down approach,
        - because we are seeking the solution from top to down
        - Though finally solution is aggregated later

    Time: O(2^n)
    Space: O(max(m,n)) Stack space
    """
    if i == len(s1) or j == len(s2):
        return 0

    if s1[i-1] == s2[j-1]:
        count = 1 + longest_common_substring_backtrack(s1, s2, i+1, j+1, count)

    else:
        count = max(count,
                    max(longest_common_substring_backtrack(s1, s2, i+1, j, count),
                        longest_common_substring_backtrack(s1, s2, i, j+1, count)))

    return count


def longest_common_substring_memoization(s1, s2, i, j, count, cache):
    """
    Cache to avoid unnecessary combinations

    Time: O(n^2)
    Space: O(m*n) Cache space
    """

    if i == len(s1) or j == len(s2):
        return 0

    if cache[i][j] != -1:
        return cache[i][j]

    if s1[i-1] == s2[j-1]:
        count = 1 + longest_common_substring_memoization(s1, s2, i+1, j+1, count, cache)

    else:
        count = max(count,
                    max(longest_common_substring_memoization(s1, s2, i+1, j, count, cache),
                        longest_common_substring_memoization(s1, s2, i, j+1, count, cache)))

    cache[i][j] = count
    return cache[i][j]


def longest_common_substring_iterative_bottom_up(s1, s2):
    """
    Called bottom up because
        - solution for i'th is built using solution for (i-1)'th
        - Unlike above, where solution is sought top down
    """

    cache = [[0] * (len(s2)+1) for _ in range(-1, len(s1))]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):

            if s1[i-1] == s2[j-1]:

                # previous count is cache[i-1][j-1]
                cache[i][j] = cache[i-1][j-1] + 1
            else:
                cache[i][j] = max(cache[i-1][j-1],
                                  max(cache[i-1][j],
                                      cache[i][j-1]))

    return cache[-1][-1]


if __name__ == "__main__":
    sys.setrecursionlimit(5000)

    s1 = "bundbunfbunghfredgdfsdfsdfsdfsdfsfsfsfsdfsdfaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaannnnnnnnnnnnnnnnnnnnnnniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiirrrrrrrrrrruuuuuddddhhhhhhhhhhhhhhhhbundbunfbunghfredgdfsdfsdfsdfsdfsfsfsfsdfsdf"
    s2 = "fsdfwwfsdfsdfnsdjfsdjfksdjfsdjkfsdjhfsjdfhjsdfjksdfjsdjfhweurweoirwoopeweriwepoirwejnksdsdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaannnnnnnnnnnnnnnnnnnnnnniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiirrrrrrrrrrruuuuuddddhhhhhhhhhhhhhhhhfsdfwwfsdfsdfnsdjfsdjfksdjfsdjkfsdjhfsjdfhjsdfjksdfjsdjfhweurweoirwoopeweriwepoirwejnksdsd"

    common = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaannnnnnnnnnnnnnnnnnnnnnniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiirrrrrrrrrrruuuuuddddhhhhhhhhhhhhhhhh"

    # longest_common_substring_backtrack(s1, s2, 0, 0, 0)

    print("Top down...")
    start = time.time_ns()
    cache = [[-1] * len(s2) for _ in range(len(s1))]
    print(longest_common_substring_memoization(s1, s2, 0, 0, 0, cache))
    print((time.time_ns() - start) / 1000000000)

    print("\nBottom up...")
    start = time.time_ns()
    cache = [[-1] * len(s2) for _ in range(len(s1))]
    print(longest_common_substring_iterative_bottom_up(s1, s2))
    print((time.time_ns() - start) / 1000000000)
