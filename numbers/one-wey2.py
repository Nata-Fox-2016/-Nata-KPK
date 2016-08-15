N = 4
m1 = None
for i in range(N):
    x = int(input())
    if x%2 == 0:
        if m1 == None or x > m1:
            m1 = x
if m1 != None:
    print('maksimalnoe chetnoe', m1)
else:
    print('chetnih chisel ne bilo')