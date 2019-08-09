import matplotlib.pyplot as plt
import numpy
import fastseriation.seriate

if __name__ == "__main__":

    scores = numpy.zeros((100, 10))
    for i in range(100):
        for j in range(10):
            scores[i, j] = abs(i - j)

    plt.figure()
    plt.imshow(scores, cmap='brg', interpolation='nearest', aspect='auto')
    plt.show(block=False)

    per = numpy.random.permutation(100)
    scores_pertutated = scores[per, :]

    plt.figure()
    plt.imshow(scores_pertutated, cmap='brg', interpolation='nearest', aspect='auto')
    plt.show(block=False)

    seriated_indexes = fastseriation.seriate.seriate(scores_pertutated)

    plt.figure()
    plt.imshow(scores_pertutated[seriated_indexes, :], cmap='brg', interpolation='nearest', aspect='auto')
    plt.show()
