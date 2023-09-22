A = input().split()
GLAS = ['а', 'о', 'е', 'у', 'ы', 'э', 'я', 'и', 'ю']
L_G = len(GLAS)
ans = ''
for i in range(0, len(A)):
    B = A[i]
    ANS = ''
    for j in range(0, len(B)):
        ANS += B[j]
        x = B[j]
        k = 0
        for p in range(0, L_G):
            if GLAS[p] == x:
                k += 1
        if k == 1:
            ANS += 'c' + str(B[j])
    if i == 0:
        ans += ANS
    else:
        ans += ' ' + ANS
print(ans)