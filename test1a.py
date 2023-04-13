def solution(A):
    arr = set(A)
    N = set(range(1, 100001))
    while N in arr:
       N += 1
    wyniczek = min(N - arr)
    print(wyniczek)

solution([1,2,3])
solution([-1,-3])

print("/\/\."*20)
for i in range(2,10):

    print(i)

thislist = ["apple", "banana", "cherry","pimp"]
for i in range(len(thislist)):
  print(thislist[i])

print(len(thislist))

lista_A = ['cegła', 'szklarnia', 'szpadel', 'samochód', 'bocian']
for x in lista_A:
    print (x)

for x in range(8,12):
    print('hello %s' % x)
    if x > 9:
        break
def DecimalToBinary(num):

    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')

    # Driver Code
    if __name__ == '__main__':
        # decimal value
        dec_val = 24

        # Calling function

DecimalToBinary(2345)