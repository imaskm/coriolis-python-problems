def find_longest_word(l_words):
    return reduce( lambda x,y : x if len(x)>len(y) else y , l_words )
   


print( len( find_longest_word( ['dasdas','dadad','dadasdsa' ,'adadadad'   ]  )))
