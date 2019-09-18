pokemon = 'audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'


l_pok = pokemon.split()


l = -1

for word in l_pok:
    c = 1
    flag = False
    res_l = [word]
    x = word
    while True :
        for j in l_pok:
	    if j not in res_l and j[0] == x[-1]:
		flag = True
                x = j
		res_l.append(j)
		c+=1
            else:
		flag = False
        if(flag == False):
	    break
    if(c> l):
	l = c

print res_l

print l
