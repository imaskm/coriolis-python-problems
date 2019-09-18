def is_palindrome(string):
    l = len(string)

    if(l== 0 or l== 1):
        return True
    else:
        l-=1
        i=0
        while(i<l):
	    if not string[i].isalpha():
		i+=1
		continue
            if not string[l].isalpha():
		l-=1
		continue 
            if(string[i].lower() != string[l].lower() ):
                return False
            i+=1
            l-=1
    return True



print(is_palindrome(input()))

