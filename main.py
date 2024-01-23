import numpy as np
import matplotlib.pyplot as plt

# Generate data...
x = np.random.random(10)
y = np.random.random(10)

#hello

# Plot...
plt.scatter(x, y, c=y, s=500) # s is a size of marker 
plt.gray()

plt.show()
