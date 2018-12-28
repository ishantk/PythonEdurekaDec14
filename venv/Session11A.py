import numpy as np
import matplotlib.pyplot as plt

# 100 Arrays having 100 random numbers
# X = np.random.randn(100, 100)
X = np.random.randn(1000)
print(X)

plt.hist(X, 100)
plt.show()

