string = input("Enter brackets : ")

flag = 0

ok_flag = 1

for i in string :
    if i == '[':
	flag+=1
    elif i == ']':
	flag-=1
    if(flag < 0 ):
	ok_flag = 0
        break

if(ok_flag == 0):
    print 'Not OK'

else:
    if(flag == 0):
	print "OK"
    else:
	print'Not OK'
