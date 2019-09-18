path = input("Input File")

f = open(path)

data = f.read()

f.close()

l = data.split()

print l

data = ''.join(l)
print len(data)
print len(l)

print("Average is :"+ float(len(data))/len(l)  )
