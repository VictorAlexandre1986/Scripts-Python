listas=[
    [2, 3, 5, 8, 9, 2],
    [1, 3, 5, 1, 9, 2],
    [9, 3, 5, 8, 9, 2],
]

def encontra_primeiro_duplicado(lista_inteiros):
    numeros_checados = list()
    primeiro_duplicado = -1

    for numero in lista_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado=numero
            break

        numeros_checados.append(numero)

    return primeiro_duplicado

if __name__ == '__main__':
    for lista in listas:
        print(lista, encontra_primeiro_duplicado(lista))