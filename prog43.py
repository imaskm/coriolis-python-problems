import urllib2

f =urllib2.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt')
print("Data Fetched")
def check_anagram(word1,word2):
    counter= [0]*256
    
    if(len(word1) != len(word2)):
	return False
    
    for i  in range(len(word1)):
	counter[ord(word1[i])]+=1
        counter[ord(word2[i])]-=1
    
    for l in counter:
	if(l):
	    return False
    return True	


data = f.read().split()
#data= ['asdf','dfsa','ewqewq', 'qweqwe']
l = len(data)

res_l=[]
res_fin=[]
print l
c=1
for i in range(l):
    if data[i] not in res_l:	
	x = [ data[i]]
	for j in range(i+1,l):
	    if data[j] not in res_l:
                print c
		c+=1
		if( check_anagram(data[i] , data[j] )  ):
		    res_l.append(data[j])
		    x.append(data[j])
        if(len(x) > 1 ):
	    res_fin.append(x)

print  res_fin

