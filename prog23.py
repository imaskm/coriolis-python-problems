import re

def correct(string):
   
    res = re.sub(r'\s+',' ',string.strip())
    res = re.sub(r"\.(?=\S)",'. ',res)
    print res

correct('I   am the    King.Be My Queen')
