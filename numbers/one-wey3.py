N = 4
m1 = int(input())
for i in range(N-1):
    x = int(input())
    if x%2 == 0:
        if x > m1:
            m1 = x
print('maksimalnoe chetnoe', m1)