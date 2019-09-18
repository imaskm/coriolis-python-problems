import urllib2


fil = urllib2.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt')


data = fil.read().split()
for i in data :

    w1=''
    w2=''
    k = 0
    for j in i:
        if(k%2  == 0 ):	
	    w1+=j
	    k+=1
        else:
	    w2+=j
	    k+=1
    print( i+" makes "+w1+" and "+w2 )
