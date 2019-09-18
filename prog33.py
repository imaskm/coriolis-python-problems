path = input("Enter file with path")

f = open(path)
data = f.read()

l = data.split("\n")
res =[]
for word in l:
    if( word[::-1] in l and word not in res ):
	res.append(word)
        res.append(word[::-1 ] )


print res

