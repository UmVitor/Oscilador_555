#Python version: 3.8.2
#Author: Vitor Barreto.

def converte_res(r):
    if(1000 <= r <= 999999):
        num = r/1000
        r_aux = str(num) + " K" + u'\u03A9'
    elif(r >= 1e6):
        num = r/1e6
        r_aux = str(num) + " M" + u'\u03A9'
    else:
        r_aux = str(r) + " " + u'\u03A9'
    return r_aux
def converte_cap(c):
    if(1e-1 >= c >= 9.9e-3):
        num = c/1e-3
        c_aux = str(num) + " mF"
    elif( 1e-04 >= c >= 1e-07):
        num = c/1e-6
        c_aux = str(num) + " uF"
    elif(1e-07 > c >= 1e-10):
        num = c/1e-9
        c_aux = str(num) + " nF"
    elif(1e-10 >= c ):
        num = c/1e-12
        c_aux = str(num) + " pF"
    else:
        c_aux = str(c) + " F"
    return c_aux
def param_freq(F, duty=0):
    lista = list()
    matriz = list()
    val = (1.0,1.1,1.2,1.3,1.5,1.6,1.8,2.0,2.2,2.4,2.7,3.0,3.3,3.6,3.9,4.3,4.7,5.1,5.6,6.2,6.8,7.5,8.2,9.1)
    ordem_res = (1e1,1e2,1e3,1e4,1e5,1e6)
    ordem_cap = (1e-3,1e-6,1e-9,1e-12)
    for n1 in range(0,len(ordem_res)):
        for n2 in range(0,len(ordem_res)):
            for n3 in range(0,len(ordem_cap)):
                for n4 in range(0,len(val)):
                    for n5 in range(0,len(val)):
                        for n6 in range(0,len(val)):
                            RA = val[n4]*ordem_res[n1]
                            RB = val[n5]*ordem_res[n2]
                            C  = val[n6]*ordem_cap[n3]

                            if(duty > 0):
                                dc = (RB)/(RA + (2*RB))
                                if(not((duty - 0.05) <= dc and dc <= (duty + 0.05))):                                                                
                                    continue 
                            freq =  1.44/((RA + (2*RB)) * C)
                            if(freq == F):
                                lista.append(converte_res(round(RA)))
                                lista.append(converte_res(round(RB)))
                                lista.append(converte_cap(C))
                                matriz.append(lista.copy())
                                lista.clear()
    return matriz                            

frequencia = 2500
duty_cycle = 0.5
res = param_freq(frequencia, duty_cycle)

print(res)
