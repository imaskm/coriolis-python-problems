def overlapping(l1,l2):
    for i in l1 :
	for j in l2 :
	    if i == j:
		return True
    return False

print(overlapping( [2,3,4], [1,33,34] ))
