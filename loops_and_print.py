def enumerate_list(la_lista):
    lista_numerada = []
    contador = 0
    for item in la_lista:
        if item != "":
            elemento_nuevo = f"{contador}, {item}"
            lista_numerada.append(elemento_nuevo)
            contador += 1
    return lista_numerada


def enumerate_backwards(la_list):
    lista_invertida = []
    contador = 0
    for item in la_lista:
        if item != "":
            palabra_invertida = item [:: -1]
            elemento_nuevo = f"{contador}, {palabra_invertida}"
            lista_invertida.append(elemento_nuevo)
            contador +=1
    return lista_invertida
