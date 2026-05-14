import math
import random

i1 = 0.05
i2 = 0.10

w1 = random.uniform(-0.5, 0.5)
w2 = random.uniform(-0.5, 0.5)
w3 = random.uniform(-0.5, 0.5)
w4 = random.uniform(-0.5, 0.5)
w5 = random.uniform(-0.5, 0.5)
w6 = random.uniform(-0.5, 0.5)
w7 = random.uniform(-0.5, 0.5)
w8 = random.uniform(-0.5, 0.5)

b1 = 0.5
b2 = 0.7

t1 = 0.01
t2 = 0.99

net_h1 = (w1 * i1) + (w2 * i2) + b1
net_h2 = (w3 * i1) + (w4 * i2) + b1

out_h1 = math.tanh(net_h1)
out_h2 = math.tanh(net_h2)

net_o1 = (w5 * out_h1) + (w6 * out_h2) + b2
net_o2 = (w7 * out_h1) + (w8 * out_h2) + b2

o1 = math.tanh(net_o1)
o2 = math.tanh(net_o2)

error1 = 0.5 * ((t1 - o1) ** 2)
error2 = 0.5 * ((t2 - o2) ** 2)

total_error = error1 + error2

print("w1 =", w1)
print("w2 =", w2)
print("w3 =", w3)
print("w4 =", w4)
print("w5 =", w5)
print("w6 =", w6)
print("w7 =", w7)
print("w8 =", w8)

print("o1 =", o1)
print("o2 =", o2)

print("Total Error =", total_error)
