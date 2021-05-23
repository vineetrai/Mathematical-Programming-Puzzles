import math
import numpy as np

# Source: https://realpython.com/python-rounding/#rounding-up
def round_half_up(n, decimals=3):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

vec = np.vectorize(round_half_up)

ls = []
for N in range(1,1000):
    if N % 100 == 0:
        print(N)
    H = [x for x in range(int(0.95*N**2/250),int(1.10*N**2/250))]
    H = np.asarray(H)
    H = H/(4*N)
    if len(H) == 0:
        ls.append(N)
    if len(H) > 0:
        if not any(vec(H)==N/1000):
            ls.append(N)
