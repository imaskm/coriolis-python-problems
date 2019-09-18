def max_in_list(l):
    if l is not None :
	m = l[0]
        for i in l:
	    if i > m:
		m = i
	print m
    else:
	print("List is Empty")

max_in_list([23,45,123,2,43434,3])
