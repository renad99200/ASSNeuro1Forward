import math
import random

i1 = 0.05
i2 = 0.10


b1 = 0.5
b2 = 0.7

w1 = random.uniform(-0.5, 0.5)
w2 = random.uniform(-0.5, 0.5)
w3 = random.uniform(-0.5, 0.5)
w4 = random.uniform(-0.5, 0.5)
w5 = random.uniform(-0.5, 0.5)
w6 = random.uniform(-0.5, 0.5)
w7 = random.uniform(-0.5, 0.5)
w8 = random.uniform(-0.5, 0.5)

net_h1 = (w1 * i1) + (w2 * i2) + b1
net_h2 = (w3 * i1) + (w4 * i2) + b1

out_h1 = math.tanh(net_h1)
out_h2 = math.tanh(net_h2)

net_o1 = (w5 * out_h1) + (w6 * out_h2) + b2
net_o2 = (w7 * out_h1) + (w8 * out_h2) + b2

o1 = math.tanh(net_o1)
o2 = math.tanh(net_o2)

print("Output o1 =", o1)
print("Output o2 =", o2)