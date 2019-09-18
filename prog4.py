
def is_vowel(c):
    c = c.lower()   

    if(c=='a' or c== 'e' or c== 'i' or c=='o' or c == 'u' ):
       return True
    else:
       return False

c = input("Enter one  Character:  ")[0]

print(is_vowel(c))
