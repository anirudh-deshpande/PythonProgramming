def find_L(A, k, high):
    low = 0

    while low <= high:
        mid = low + (high - low) // 2
        if A[mid] < k:
            low = mid+1
        else:
            high = mid-1

    return low


def find_U(A, k, low):
    high = len(A) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if A[mid] > k:
            high = mid-1
        else:
            low = mid+1
    return high


def interval(A, k):
    low, L, high, U = 0, -1, len(A)-1, -1

    while low <= high:
        mid = low + (high-low) // 2

        if A[mid] == k:
            L = find_L(A, k, mid)
            U = find_U(A, k, mid)
            break
        elif A[mid] < k:
            low = mid+1
        else:
            high = mid-1

    return [L, U]

if __name__ == "__main__":
    A = [1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7]
    L, R = interval(A, 13)
    print(L, R, A[L], A[R])

