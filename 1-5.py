N, b, c = list(map(int, input().split()))
N1 = str(N)
A = 0
for i in range(0, len(N1)):
    A += int(N1[len(N1) - 1 - i]) * (b ** i)
x = 0
while c ** x < A:
    x += 1
Ans = ''
while x != -1:
    if A >= c ** x:
        k = A // (c ** x)
        Ans += str(k)
        A -= c ** x * k
    x -= 1
print(int(Ans))