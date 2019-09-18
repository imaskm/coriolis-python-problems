
l = list ( map (int , input().split() ) )


#print('Select one operation : ')
#print("1.  Sum ")
#print('2   Product')

#ch = input()

#if(ch  not in '12'):
#    print("Enter a valid value ")
#else:
#    ch = int(ch)
#    if(ch == 1 )

def sum_list(l):
    s = 0
    for i in l :
       s+=i
    return s

def product(l):
    p = 1
    for i in l:
	p*=i
    return p

print("Sum : "+str(sum_list(l) ) +"\nProduct : "+str(product(l))  )   
