def get_len(var):
    
    l = 0
    
    for i in var:
	l+=1
    return l

var = ( input("Enter a String"))

print(get_len(var))
