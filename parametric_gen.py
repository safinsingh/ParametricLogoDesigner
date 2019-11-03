import matplotlib.pyplot as plt
import numpy as np

val1 = int(input("Val1: "))
val2 = int(input("Val2: "))
precs = int(input("Precision (1-10): "))

n = 1000*precs
t = np.linspace(0, 2*np.pi, n+1)

x = np.cos(val1*t)
y = np.sin(val2*t)

plt.axis("equal")
plt.grid()
plt.plot(x, y)
plt.show()