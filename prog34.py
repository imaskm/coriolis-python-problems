def char_freq(string):
    counted = ''
    count_dict={}
    for i in string:
	if i not in counted:
	    counted+=i
            count_dict.update( { i : string.count(i)  }   )
    
    return count_dict

path = input("Enter File")

f = open(path)

data = f.read()

f.close()

d = char_freq(data)

for key in sorted(d.iterkeys()):
    print key, "  ",d[key]



