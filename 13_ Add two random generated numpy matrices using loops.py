# create random matrix of size 5*4

import numpy as np
a1 =  np.random.rand(5,4)

print(a1)
print("************************************************")
print("shape of this matrices", a1.shape)

a2 =  np.random.rand(5,4)

print(a2)
print("************************************************")
print("shape of this matrices", a2.shape)

print("************************************************")

b= a1 + a2
print(b)