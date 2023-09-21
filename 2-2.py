G = int(input())
A = str(input())
A1 = ''
for i in range(0, len(A) // G):
    B = A[(len(A) // G) * i: (len(A) // G) * (i+1):][::-1]
    A1 += B
print(A1)
