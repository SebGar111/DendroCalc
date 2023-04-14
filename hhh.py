# def is_sparse(N):
#     """
#     Returns True if the binary representation of n is sparse, False otherwise.
#     """
#     pass
#
#
# def solution(N):
#     """
#     Returns any integer that is one part of a sparse decomposition of N.
#     Returns -1 if there is no sparse decomposition of N.
#     """
#     binary = bin(N)[2:]
#     for i in range(1, len(binary)):
#         if binary[i] == "1" and binary[i - 1] == "1":
#             return False
#     return True
#     for i in range(1, N):
#         if sp(i) and sp(N-i):
#             return i
#     return -1
#
# print(solution(30))
#
#
#
# for i in range(10):
#     if i == 9:
#         print("pimpek")
#
#     print(i)

# def sol(A):
#
#     Array=[1,(A)[-1]]
#
#     sortA=sorted(A)
#
#     for (i) in range(min(A[0]),max(A[-1])):
#         int(i)
#         if i <= 0:
#             return 1
#         elif i >0 and A[-1]> len(A):
#             return min(Array.pop(A))
#         else:
#             return A[-1]+1
#
#
# print(sol([3,5,5,7]))


def solution(a):
    segments = {}  # dictionary to store the segments

    for i in range(len(a) - 1):
        segment_sum = a[i] + a[i + 1]  # calculate the sum of the segment

        if segment_sum in segments:
            # if a segment with this sum already exists, check if it intersects
            if i <= segments[segment_sum][-1]:
                continue  # skip if it intersects

        # add the segment to the dictionary
        if segment_sum in segments:
            segments[segment_sum].append(i)
        else:
            segments[segment_sum] = [i]

    # count the number of non-intersecting segments with equal sums
    count = 0
    for key in segments:
        count += len(segments[key])

    return count



print(solution([4,5,3,5]))

