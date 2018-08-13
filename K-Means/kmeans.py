import numpy as np

mydata = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]


def find_clusters(data=[], k=1):
    result = np.zeros((2,7), dtype=np.float)

    for i in range(1, k):
        for x in data:
            d = ((x - k) ** 2) ** (1 / 2)

    print(result)


find_clusters(mydata, 2)