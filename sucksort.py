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
    print numbers
    # Get idx of smallest.
    min_idx = mindex(numbers[i:])
    # Pop it, place in front
    numbers.insert(0,numbers.pop(i+min_idx))
    i += 1
  return numbers
