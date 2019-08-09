import numpy

def seriate(A):

    K = numpy.cumsum(A)

    print(K)
    
    print(type(K))
    
    K = K[1]

    print(K)

    # D = diag(K)
    # L = D-A

    return K