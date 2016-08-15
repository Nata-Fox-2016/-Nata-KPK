N = int(input())
# schitivaem v ochered pervie 6 chisel
Q = [int(input()) for i in range(6)]
min_even = 1001
beta = 1000001
for i in range(N-6):
    # pervii element pokidaet ochered
    x = Q[0]
    min_x = min(min_x, x)
    if x%2 == 0 and x < min_even:
        min_even = x
    x = int(input())
    beta = min(beta, x*min_even)
    if x%2 == 0:
        beta = min(beta, x*min_even)

    Q.pop(0)
    Q.append(x)