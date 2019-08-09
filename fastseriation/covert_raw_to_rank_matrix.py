import numpy


def convert_raw_to_rank_matrix(M):
    [nr, nc] = M.shape
    # print(nr)
    # print(nc)

    R = numpy.zeros((nr, nc))

    for i in range(0, nc):
        I = numpy.argsort(M[:, i])
        R[I[0], i] = 0
        sharing = 0
        sharing_list = []
        for j in range(1, nr):
            R[I[j], i] = j
            if M[I[j], i] != M[I[j - 1], i]:
                R[I[j], i] = j
                if sharing != 0:
                    val = sharing / len(sharing_list)
                    R[sharing_list, i] = val
                    sharing = 0
                    sharing_list = []
            else:
                if sharing == 0:
                    sharing = j + j - 1
                    sharing_list = [I[j-1], I[j]]
                else:
                    sharing = sharing + j
                    sharing_list.append(I[j])
        if sharing != 0:
            val = sharing / len(sharing_list)
            R[sharing_list, i] = val

    return R
