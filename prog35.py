from gtts import gTTS
import pyttsx3
import os
import time

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}


text = str(input("Enter Text : \n ").lower())

res=''
ngine = pyttsx3.init()

for i in text:
   
    ngine.say(d[i])
    time.sleep(0.23)

#my_obj= gTTS(text = text , lang = 'en' ,slow= False)

#my_obj.save("Wel.mp3")
ngine.runAndWait()
#os.system( "wel.mp3" ) 
