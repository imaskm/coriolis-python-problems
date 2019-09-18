path =  input("Enter File")

f = open(path)

data = f.read()

f.close()

l = data.split()

l = map( str.lower , l  )

res = []

for i in range(len(l)) :
    if(i==0 and l[i] not in l[1 : ]  ):
	res.append(l[i])
    elif(i==len(l)-1 and l[i]  not in l[0:i]  ):
	res.append(l[i] ) 

    elif( l[i] not in l[i+1:] and l[i] not in l[0:i]   ):
	res.append(l[i])

print res
 
