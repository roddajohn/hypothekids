import numpy

data = numpy.genfromtxt('../data/gpas.csv', delimiter=',', skip_header=1)

for i in range(0, 3):
    working = data[:,i]

    print(numpy.median(working))
    print(numpy.mean(working))
    print(numpy.std(working))
    print(numpy.var(working))    
