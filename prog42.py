

data = 'Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn''t. In any case, this isn''t true... Well, with a probability of .9 it isn''t.'

for i in range( len( data ) ):
    if( (data[i] == '.' or data[ i ] == '!' or data[i] == '?') and i < len(data)-1  ):
	if( i < len(data )-2 and data[i+1] == ' ' and data[i+2] == data[i+2].upper() and i !=2 ):
	    if(i<len(data)-4 and data[i+3]==data[i+3].lower() and data[i+4] =='.'):
		print (data[i],end='')
	    else:
		print (data[i])
        else:
	    print( data[i], end ='')
    else:
	print( data[i],end='')
    
	
