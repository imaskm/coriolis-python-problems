def make_3sg_form(string):
   res=''
   if(string.endswith('y') or string.endswith('Y') ):
	res+=string[0:-1]+'ies'
   elif(string[-1].lower() == 'o' or string.lower().endswith('ch') or string.lower()[-1] == 's' or  string.lower()[-1] == 'x' or  string.lower()[-1] == 'z' or string.lower().endswith('sh')  ):
	res+=string+'es'
   else:
	res+=string+'s'
   return res



print(make_3sg_form('love'))
