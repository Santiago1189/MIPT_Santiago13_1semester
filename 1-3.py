A = list(map(int, input().split()))
n = len(A)
x = 1
for i in range(n):
    x *= A[i]
x1 = x ** (1 / n)
print(x1)