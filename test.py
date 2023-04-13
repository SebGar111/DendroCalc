print("hello")

A = [-1, 6]
n = 0
def solution():
    if sorted(A)[-1] < 0:
        n = 1
        print(n)

    elif sorted(A)[-1] > 0:
        n = sorted(A)[-1] +1
        print(n)



    #n = n >0 and n not in A
    #print(n)

solution()


print(sorted(A))