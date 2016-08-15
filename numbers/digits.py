x = int(input())
n = 0
s = 0
p = 1
while x:
    digit = x%10
    n += 1
    s += digit
    p *= digit

    x //= 10

print('kolichestvo cifr:', n)
print('summa cifr:', s)
print('proizvedenie cifr:', p)
print('srednee arifmeticheskoe:', s/n)
