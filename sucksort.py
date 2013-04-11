import random
import timeit

def sucksort(numbers):
  i = 0
  # Returns the index of the minimal element in a list
  def mindex(tail):
    idx = 0
    smallest = tail[0]
    i = 0
    while i < len(tail):
      if tail[i] < smallest:
        idx = i
        smallest = tail[i]
      i += 1
    return idx
  # Now go through, grab the smallest element, place it at the head. Repeat.
  while i < len(numbers):
    # Get idx of smallest.
    min_idx = mindex(numbers[i:])
    # Pop it, place in front
    numbers.insert(0,numbers.pop(i+min_idx))
    i += 1
  return numbers

def random_number_list(n):
  x = []
  i = 0
  while i < n:
    x.append(random.randrange(-100,100))
    i += 1
  return x

def test(n):
        rn = random_number_list(n)
        sucksort(rn)

if __name__ == '__main__':
    import timeit
    print "Sorting random list of size 1     : ", timeit.timeit("test(1)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 10    : ", timeit.timeit("test(10)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 100   : ", timeit.timeit("test(100)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 1000  : ", timeit.timeit("test(1000)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 2000  : ", timeit.timeit("test(2000)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 3000  : ", timeit.timeit("test(3000)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 5000  : ", timeit.timeit("test(5000)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 10000 : ", timeit.timeit("test(10000)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 100000: ", timeit.timeit("test(10000)", setup="from __main__ import test", number=1),"s"
    print "Finished!"
