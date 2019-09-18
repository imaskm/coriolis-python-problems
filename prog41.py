
from __future__ import print_function
word = 'tiger'

guess = input("Guess a 5 letter Word :")[:5]

while(guess != word):
    res = ''
    for i in range(len(guess)):
	if( i< len(word)):
            if(guess[i] in word ):
		if(word[i] == guess[i] ):
		    res+='['+guess[i]+']'
		else:
		    res+='('+guess[i]+')'
            else:
		res+=guess[i]
    print( 'Clue : '+ res)
    guess = input("Guess a 5 letter Word :")[:5]

for i in guess:
    print('['+i+']',end='' )
    
