def map(func,itrtr):
    res = []
    for i in itrtr:
	res.append(func(i))
    return res

def filter(func,itrtr):
    res = []
    for i in itrtr:
	if( func(i)  ):
	    res.append(i)

    return res


def reduce(func,itrtr):
    for i in range(len(itrtr) - 1 ):
	if(i==0 and len(itrtr) >=2 )  :
	    res = func(itrtr[i] , itrtr[i+1] )
        else:
	    res = func(res,itrtr[i+1])
    return res

l = [23,34,12,78,34,56]
print(filter(lambda x:True if x > 30 else False ,l))
