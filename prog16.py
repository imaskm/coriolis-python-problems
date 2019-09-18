def filter_long_words(words,n):
    i = 0
    while i < (len(words)):
	if(len(words[i]) < n) :
	    del words[i]
        else:
	    i+=1
    print words


filter_long_words(['z','qwerty','asdf','a'],2)

