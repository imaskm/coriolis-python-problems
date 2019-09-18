def reverse_str(string):
    
    l = len(string)
    l-=1
    
    rev=''
    while(l>=0):
	rev+= string[l]
        l-=1
    return rev

s = input('Enter String to Reverse')

print(reverse_str(s))
