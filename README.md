# fastseriation

[![license: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/avramidis/fastseriation/blob/master/LICENSE)

fastseriation is a Python package that can be used to seriate matrices.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To get the code you will need git. To install git on Ubuntu use the following commands in a terminal

```
sudo apt update
sudo apt install git
```

To clone the repository from github use the following command in a terminal

```
git clone https://github.com/avramidis/fastseriation.git
```

To run the code you will need Python version 3, to install it use the following command in a terminal

```
sudo apt install python3
```

### Installing

To install fastseriation package use the following command in a terminal

```
python3 setup.py install
```

### Example

An example code that uses fastseriation is the following

```python
import matplotlib.pyplot as plt
import numpy
import fastseriation.seriate
from scipy.spatial.distance import pdist
from seriate import seriate

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
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* The implementation of the seriation method is based on the code in https://github.com/fieldsend/emo_2013_viz