import numpy
import fastseriation.covert_raw_to_rank_matrix
import fastseriation.get_similarity_matrix


def seriate(input_matrix):
    rank_matrix = fastseriation.covert_raw_to_rank_matrix.convert_raw_to_rank_matrix(input_matrix)
    similarity_matrix = fastseriation.get_similarity_matrix.get_similarity_matrix(rank_matrix)

    K = numpy.cumsum(similarity_matrix, axis=0)
    K = K[-1, :]
    D = numpy.diag(K)
    L = D - similarity_matrix

    eigen_values, eigen_vectors = numpy.linalg.eig(L)
    fiedler_vector = eigen_vectors[:, 1]
    permutation = numpy.argsort(fiedler_vector)

    return permutation
