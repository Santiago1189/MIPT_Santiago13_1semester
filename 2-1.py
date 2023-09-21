A = list(map(int, input().split()))
n = A[0]
ans = n * (n + 1) // 2
for i in range(1, n):
    ans -= A[i]
print(ans)
