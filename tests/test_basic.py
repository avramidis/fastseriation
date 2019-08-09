import unittest
import sys

sys.path.append('../fastseriation')
import fastseriation.covert_raw_to_rank_matrix
import fastseriation.get_similarity_matrix
import fastseriation.seriate
import numpy


class TestFastSeriationMethods(unittest.TestCase):

    def test_fastseriation_1(self):

        scores_original = numpy.zeros((10000, 10))
        for i in range(100):
            for j in range(10):
                scores_original[i, j] = abs(i - j)

        per = numpy.random.permutation(10000)
        scores = scores_original[per, :]

        R = fastseriation.covert_raw_to_rank_matrix.convert_raw_to_rank_matrix(scores)
        S = fastseriation.get_similarity_matrix.get_similarity_matrix(R)
        scores_seriated = fastseriation.seriate.seriate(S)

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
