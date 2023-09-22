a = input().split()
max = 0
for i in range(0, len(a)):
    if a.count(a[i]) > max:
        max = a.count(a[i])
for j in range(0, len(a)):
    if a.count(a[j]) == max:
        print(a[j])
        break
