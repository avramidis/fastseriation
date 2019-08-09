import numpy


def get_similarity_matrix(M):
    [nr, nc] = M.shape
    # print(nr)
    # print(nc)

    S = numpy.zeros((nr, nr))

    for i in range(nr):
        for j in range(nr):
            S[i, j] = 1 - (1 / (nc * (nr - 1) ** 2)) * sum((M[i, :] - M[j, :]) ** 2)

    return S
