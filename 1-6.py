def gopa(a, o):
    l = len(str(a))
    g = a
    x = 0
    for j in range(0, l):
        x += g % 10 * (o ** j)
        g = g // 10
    return x

f = open('input.TXT')
A = f.readlines()
N = list(map(int, A[0].split()))
O = int(A[2])
x = A[1].split()[0]
print(x)
for i in range(0, len(N)):
    N[i] = gopa(N[i], O)
if x == '*':
    ans = 1
    for i in range(0, len(N)):
        ans *= N[i]
elif x == '+':
    ans = 0
    for i in range(0, len(N)):
        ans += N[i]
else:
    ans = N[0]
    for i in range(1, len(N)):
        ans -= N[i]
print(ans)
output = open('output.TXT', 'w')
print(ans, file = output)