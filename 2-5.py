a = input().split()
print(*(a[len(a) - 1:]+a[:len(a) - 1]))