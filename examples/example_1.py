import matplotlib.pyplot as plt
import numpy
import fastseriation.seriate
from scipy.spatial.distance import pdist
from seriate import seriate

if __name__ == "__main__":

    scores = numpy.zeros((100, 10))
    for i in range(100):
        for j in range(10):
            scores[i, j] = abs(i - j)

    plt.figure()
    plt.imshow(scores, cmap='brg', interpolation='nearest', aspect='auto')
    plt.show(block=False)

    per = numpy.random.permutation(100)
    scores = scores[per, :]

    seriated_indexes = fastseriation.seriate.seriate(scores)

    plt.figure()
    plt.imshow(scores[seriated_indexes, :], cmap='brg', interpolation='nearest', aspect='auto')
    plt.show(block=False)

    plt.figure()
    plt.imshow(seriate(pdist(scores)), cmap='brg', interpolation='nearest', aspect='auto')
    plt.show()
