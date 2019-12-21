def local_minima(A):
    low , high = 0, len(A) - 1
    result = 0

    while low <= high:

        mid = low + (high-low) // 2

        if A[mid] <= A[mid-1]:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return -1 if result > len(A) else result

if __name__ == "__main__":
    A = [7,6,5,5,5,4,4,4,4,3,3,2,2,2,2,1,1,1,0,1,2,3,4,5,6,7,7,7,8,8,9]
    B = [1,2,3,4,5]
    C = [5,4,3,2,1]

    print(C[local_minima(C)])
