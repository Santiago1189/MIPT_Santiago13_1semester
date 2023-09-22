f = open("input.TXT", 'r')
a = f.read()
l = len(a)
A = f.readlines()
l_A = len(A) - 1
B = []
for i in range(0, l):
    if a[i] != ' ':
        B.append(a[i])
print(B)
while '.' in B:
    x = B.index('.')
    B[x] = ' '
while '!' in B:
    x = B.index('!')
    B[x] = ' '
while '?' in B:
    x = B.index('?')
    B[x] = ' '
print(B)
ans = 0
for k in range(0, len(B) - 1):
    if B[k] != ' ' and B[k + 1] == ' ':
        ans += 1
print(ans)
