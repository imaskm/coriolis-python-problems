

dict_1 = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

def translate(eng):
    global dict_1
    return dict_1[eng]


print(map( translate , ['merry' ,'christmas']   ))
