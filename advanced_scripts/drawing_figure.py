import matplotlib.pyplot as plt


x = [i for i in range(1, 16)]
APPROX_NONE = [6, 1, 1912, 1911, 5171, 7, 1288, 1285, 1222, 1218, 1637, 1632, 2066, 373, 10]
APPROX_SIMPLE = [6, 1, 877, 890, 2555, 6, 116, 119, 46, 46, 836, 844, 212, 31, 8]
APPROX_TC89_L1 = [2, 1, 393, 401, 1220, 2, 54, 55, 26, 24, 402, 401, 104, 15, 3]
APPROX_TC89_KCOS = [2, 1, 328, 321, 1008, 2, 53, 54, 24, 22, 286, 284, 100, 12, 3]

plt.plot(x, APPROX_NONE, )
plt.plot(x, APPROX_SIMPLE)
plt.plot(x, APPROX_TC89_L1)
plt.plot(x, APPROX_TC89_KCOS)
plt.xlabel('Number of contour')
plt.ylabel('Amount of points')
plt.show()
