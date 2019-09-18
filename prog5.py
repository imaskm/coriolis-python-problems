def translate(line):
   
    res= ''
    for i in line :
    
	if(i.lower() in 'bcdfghjklmnpqrstvwxyz'):
	     
	    res+=i
            res+='o'
            res+=i
        else:
            res+=i
    
    return res

line = input("Enter a String : ")

print(translate(line)) 
