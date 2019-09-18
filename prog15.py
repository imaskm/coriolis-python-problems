def find_longest_word(l):
     if l is not None :
        ll = len(l[0])
        for word in l:
	    if(len(word) > ll  ):
		ll = len(word)
	print ll
     else:
	print("Empty List")

find_longest_word(['dasdasd','cxzvxcvzxc','erwetwetwetewt'])
			  
    
