

mumbers = ['DEV', 'DEV', 'DEV', 'DEV', 'DEV', 'DEV', 'DIR', 'CDP', 'CDP', 'DEV']

def calc(mumb):
    schoko_b_grame = 0
    moyen_schoko_b = 2
    
    if mumb == "DEV":
        schoko_b_grame = (((moyen_schoko_b * 4)*3) * 315)
        
    elif mumb == "CDP":
        schoko_b_grame = (((moyen_schoko_b * 6)*3) * 315)
        
    elif mumb == "DIR":
        schoko_b_grame = (((moyen_schoko_b * 8)*3) * 315)
        
    if mumb =="DIR":
        schoko_b_grame += (20*2)*45
    else:
        schoko_b_grame += 20*45
    
    return (schoko_b_grame/1000)


sum = 0
for mumb in mumbers:
    sum += calc(mumb)





print(f"{sum:.2f}kg")