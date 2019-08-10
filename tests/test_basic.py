import unittest
import sys
import numpy

sys.path.append('..')
import fastseriation.seriate


class TestFastSeriationMethods(unittest.TestCase):

    def test_fastseriation_1(self):

        nrows = 10
        ncols = 2

        scores = numpy.zeros((nrows, ncols))
        for i in range(nrows):
            for j in range(ncols):
                scores[i, j] = abs(i - j)

        per = numpy.random.permutation(nrows)
        scores_pertutated = scores[per, :]
        seriated_indexes = fastseriation.seriate.seriate(scores_pertutated)

        result = False

        if numpy.array_equiv(scores, scores_pertutated[seriated_indexes, :]):
            result = True

        if numpy.array_equiv(scores, numpy.flipud(scores_pertutated[seriated_indexes, :])):
            result = True

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
