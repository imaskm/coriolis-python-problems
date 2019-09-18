dict_eng_to_swed = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

def translate(l_eng):
   l_swed = []
   
   for eng in l_eng:
	l_swed.append(dict_eng_to_swed[eng].lower())
   return l_swed


print(translate(["merry","christmas"]))
