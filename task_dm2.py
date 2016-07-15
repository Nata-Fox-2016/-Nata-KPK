from drawman import *
from time import sleep

from drawman import drawman_scale

def f(x):
    return x*x

print (drawman_scale)
drawman_scale (10)
x = -4.5
to_point(x, f(x))
pen_down()
while x <= 4.5:
    to_point(x, f(x))
    x += 0.1
pen_up()

sleep(10)