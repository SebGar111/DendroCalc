def solution(A, K):
    n = len(A)
    i = 0
    for num in range(1, K+1):
        if num not in A:
            return False
        while i < n and A[i] < num:
            i += 1
        if i == n or A[i] > num:
            return False
    return True


print(solution([1,3],2))