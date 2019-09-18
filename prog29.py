
def filter_long_words(l_words,n):

    return filter( lambda x : True if len(x) > n else False, l_words  )
    


print(filter_long_words( ['sadas','dasdsad','gdgd','a' ,'dasd','e','dad'   ],2  )) 
