l_words = ['asdsaf','dasdasda','dasdas']

l_length = []
for i in l_words:
    l_length.append(len(i))

print l_length
l_length = []

print(map( lambda x : len(x), l_words   )) 

print  [ len(x)  for x in l_words  ] 

