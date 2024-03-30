import doctest
import statistics

def square(n):
    """
    >>> square(9)
    81
    """
    return (n**2)




def stats(numbers):
    """
    >>> stats([1,3,5])
    (3, 3, 2.0)
    """
    return statistics.mean(numbers), statistics.median(numbers), statistics.stdev(numbers)

doctest.testmod(verbose=True)