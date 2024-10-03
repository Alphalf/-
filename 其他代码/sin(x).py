import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,1000)
y1=np.sin(x)
y2=np.sin(x**2)
plt.figure(figsize=(8,4))

plt.title("sin(x) and sin(x**2)")
plt.plot(x,y2,label="sin(X**2)")

plt.ylim(-1.5,1.5)
plt.xlim(0,10)
plt.legend()

plt.show()
