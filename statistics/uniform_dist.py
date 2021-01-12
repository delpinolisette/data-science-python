# problem: calculate the distance between any two points in a uniform random distribution. 
# problem sourced from @ben257

import numpy as np


distances = []

for x in range(200000):
    x_1 = np.random.uniform()
    print(x_1)
    x_2 = np.random.uniform()
    print(x_2)

    # distance from these two points. 
    dist = abs(x_1 - x_2)
    print("distance is", dist)
    distances.append(dist)

# now get average distance
sum = 0
for x in distances:
    sum += x

print("avg is :", (sum)/len(distances))




