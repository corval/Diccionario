import itertools

cadena = "Contraseña321"

for n in range(0, len(cadena) + 1):
    texto = cadena[0:n]
    nuevo = itertools.permutations(texto)
    for permutacion in nuevo:
        print(''.join(permutacion))

    combinaciones = itertools.combinations(cadena, n)
    for combinacion in combinaciones:
        print(''.join(combinacion))
