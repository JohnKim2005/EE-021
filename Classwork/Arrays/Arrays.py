import numpy as np
n = 5
nrow = 5
ncol = 5
a = np.empty([nrow,ncol])
print(a)
for i in range(nrow):
    for j in range(ncol):
        print(i,j)
        a[i,j] = i+j
        print(a[i,j])