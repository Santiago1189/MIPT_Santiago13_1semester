f = open("text.TXT", 'r')
A = f.readlines()
B = list(map(int, A[0].split()))
print(A[1])
if A[1] == '*':
    ans = 1
    for i in range(0, len(B)):
        ans *= B[i]
    print(ans)
elif A[1] == '+':
    ans = 0
    for i in range(0, len(B)):
        ans += B[i]
    print(ans)
else:
    ans = B[0]
    for i in range(1, len(B)):
        ans -= B[i]
    print(ans)

