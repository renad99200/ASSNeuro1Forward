import math

w1 = 0.15
w2 = 0.20
w3 = 0.25
w4 = 0.30
w5 = 0.40
w6 = 0.45
w7 = 0.50
w8 = 0.55

i1 = 0.05
i2 = 0.10

out_h1 = 0.4834
out_h2 = 0.4949

o1 = 0.8062
o2 = 0.8379

t1 = 0.01
t2 = 0.99

lr = 0.5

delta_o1 = (o1 - t1) * (1 - (o1 ** 2))
delta_o2 = (o2 - t2) * (1 - (o2 ** 2))

w5_new = w5 - (lr * delta_o1 * out_h1)
w6_new = w6 - (lr * delta_o1 * out_h2)

w7_new = w7 - (lr * delta_o2 * out_h1)
w8_new = w8 - (lr * delta_o2 * out_h2)

delta_h1 = (1 - (out_h1 ** 2)) * ((delta_o1 * w5) + (delta_o2 * w7))

delta_h2 = (1 - (out_h2 ** 2)) * ((delta_o1 * w6) + (delta_o2 * w8))

w1_new = w1 - (lr * delta_h1 * i1)
w2_new = w2 - (lr * delta_h1 * i2)

w3_new = w3 - (lr * delta_h2 * i1)
w4_new = w4 - (lr * delta_h2 * i2)

print("Updated Weights:")

print("w1 =", w1_new)
print("w2 =", w2_new)
print("w3 =", w3_new)
print("w4 =", w4_new)

print("w5 =", w5_new)
print("w6 =", w6_new)
print("w7 =", w7_new)
print("w8 =", w8_new)