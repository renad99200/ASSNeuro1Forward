import math

i1 = 0.05
i2 = 0.10


w1 = 0.15
w2 = 0.20
w3 = 0.25
w4 = 0.30
w5 = 0.40
w6 = 0.45
w7 = 0.50
w8 = 0.55


b1 = 0.5
b2 = 0.7


t1 = 0.1
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


print("o1 =", o1)
print("o2 =", o2)
print("Total Error =", total_error)