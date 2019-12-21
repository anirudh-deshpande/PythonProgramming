def search_gt_k(A, k):

    low, high = 0, len(A)-1

    while low <= high:
        mid = low + (high - low) // 2

        if A[mid] == k:
            low = mid+1 # what should I do here?, this pgm, its low = mid + 1
        elif A[mid] > k:
            high = mid-1
        else:
            low = mid+1

    return low

if __name__ == "__main__":
    A = [-2, -2, 0, 0, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
    print(A[search_gt_k(A, -13)])
