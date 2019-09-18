from functools import reduce
l = [23,34,12,78,34,56]
print(reduce(lambda x,y:x if x > y else y,l))
