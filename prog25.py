def make_ing_form(verb):
    if(len(verb) < 2):
	return "invalid Verb"
    res = ''
    if(verb[-1].lower() == 'e'):
	if(len(verb) == 2 or verb[-2] == 'e'):
	   res+=verb+'ing'
        else:
           res+=verb[0:-1]+'ing'
    elif( verb.lower().endswith('ie')) :
	res+=verb[0:-2]+'ying'
    elif( len(verb) >=3 and ( verb[-3].lower() in 'qwrtysdfghjklzpxcvbnm' and verb[-2].lower()  in 'aeiou' and verb[-1].lower() in 'qwrtypsdfghjklzxcvbnm' ) ):
	res+=verb+verb[-1]+'ing'
    else:
	res+=verb+'ing' 


    return res


print(make_ing_form( input()  ))
