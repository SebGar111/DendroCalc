def max_gap(N):
    xs = bin(N)[2:]
    xd=xs.strip('0')
    xd=xs.split('1')
    return max([len(x) for x in xd])

print(max_gap(465030))

h=465030
h=bin(h)[2:]
print(h)


hahah='3344333344'
haha=hahah.strip('3')
print(haha)



























