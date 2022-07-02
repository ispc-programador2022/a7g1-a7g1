#función que calcula la varianza del vector obtenido en genrnd

def varianza(lstgen):
    media = sum(lstgen) / len(lstgen)
    var=0
    for i in lstgen:
        var += (i - media)**2
    print("la varianza del vector obtenido en genrnd es: ", var / (len(lstgen) -1))
    
varianza()

#aporte hecho por Marcelo Karim Juri Garay