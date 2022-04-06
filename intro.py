# https://numpy.org/numpy-tutorials/content/tutorial-svd.html

# Linear Algebra on n-dimensional arrays
# Description:This tutorial is for people who have a basic understanding of linear algebra and arrays in NumPy and want to understand how n-dimensional () arrays are represented and can be manipulated.

# We'll be doing matrix decomposition from linalg, the SVD, (to generate compressed approximation of an image)
from scipy import misc
import matplotlib.pyplot as plt

img = misc.face()
# matplotlib.pyplot imread
print(type(img))

# %matplotlib inline -> only works on ipython
plt.imshow(img)
plt.show()

print(img[:, :, 0])  # red pxs
