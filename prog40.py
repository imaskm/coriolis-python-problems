l_words = ["red",'black','blue','brown','white']
import random
w =random.choice(l_words)

anagram = ''.join( random.sample(w,len(w)  ) )


print "Color Anagram is : "+anagram

guess = input("Guess the Color :  ")

while(guess != w ):
   print "Wrong"
   guess = input("Guess the Color :  ")


print"Correct"
