

import time
import scipy as sp
import scipy.linalg as la
import numpy as np

n = 6
iterno = 7000*100

A = np.array([[3.4556,2.1234,4.567,6.777,3.456,1.345],[5.4256,1.6734,4.1267,4.7577,3.456,1.345],[2.4536,0.1234,5.547,1.737,3.456,3.325],[0.4556,0.1224,8.767,7.377,5.456,6.345],[0.4556,1.1234,2.567,7.777,6.356,2.325],[2.4356,4.1234,1.67,2.757,4.436,1.345]], dtype=np.float64, order='F')
B = np.array([[2.4356,2.1234,2.567,6.7347,3.416,1.345],[2.4256,3.6734,4.1267,5.7577,3.4126,1.31245],[1.4536,2.1234,5.5347,2.7337,4.4356,4.3425],[3.4156,7.2224,6.7167,2.1277,5.4516,2.12345],[1.4556,0.1234,2.51267,7.1777,4.356,2.3125],[1.4356,2.1234,5.67,2.7257,4.1436,2.345]], dtype=np.float64, order='F')

print(A.flags)

t = time.time()
for i in range(iterno):
    for j in range(82):
        C = np.dot(A,B)


t = time.time() - t
# f = 2*n**3/t/1e9
print("Numpy dot: time = %.2f sec; flop rate =  Gflops/s"%(t))


t = time.time()
for i in range(iterno):
    for j in range(82):
        C = sp.dot(A,B)
t = time.time() - t
# f = 2*n**3/t/1e9
print("Scipy dot: time = %.2f sec; flop rate =  Gflops/s"%(t))


t = time.time()
for i in range(iterno):
    for j in range(82):
        C = la.blas.dgemm(1.0, A, B)
t = time.time() - t
# f = 2*n**3/t/1e9
print("Scipy dgemm: time = %.2f sec; flop rate =  Gflops/s"%(t))

# print(np.__config__.show())
# print(sp.__config__.show())

