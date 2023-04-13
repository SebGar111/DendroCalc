def is_sparse(N):
    """
    Returns True if the binary representation of n is sparse, False otherwise.
    """
    pass


def solution(N):
    """
    Returns any integer that is one part of a sparse decomposition of N.
    Returns -1 if there is no sparse decomposition of N.
    """
    binary = bin(N)[2:]
    for i in range(1, len(binary)):
        if binary[i] == "1" and binary[i - 1] == "1":
            return False
    return True
    for i in range(1, N):
        if sp(i) and sp(N-i):
            return i
    return -1

print(solution(30))




