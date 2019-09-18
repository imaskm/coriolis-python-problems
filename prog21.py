def char_freq(string):
    counted = ''
    count_dict={}
    for i in string:
	if i not in counted:
	    counted+=i
            count_dict.update( { i : string.count(i)  }   )
    
    return count_dict


print( char_freq("assaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabasassdsdwewew"))
