path =  input("Input FIle Path")

f = open(path)

data = f.read()

f.close()

l = data.split("\n")
l = l[0:-1]
f_new = open( "/home/ashwanin/work/output.txt" , 'w')

for i in range (len(l)):
    f_new.write(  str(i+1)+"  "+ str(l[i])+"\n"   )


f_new.close()

print("Output File Created Successfully")
