N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(0, len(a)):
    x = a[i]
    k = 0
    for j in range(0, len(a)):
        if x > a[j]:
            k += 1
    if k == N // 2:
        ans = a[i]
print(ans)