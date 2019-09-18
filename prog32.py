def is_palindrome(string):
    l = len(string)
    
    if(l== 0 or l== 1):
        return True
    else:
	l-=1
        i=0
        while(i<l):
	    if(string[i] != string[l]):
		return False
            i+=1
	    l-=1
    return True

path = input("Enter path of file")

f = open(path)

data = f.read()

l = data.split("\n")
l=l[0:-1]
res = filter( is_palindrome , l )

print res
