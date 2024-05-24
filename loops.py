enumerate_list ():

def index_of_by_index(word, list, index):
    contador=0
    nueva_lista = lista[indice:]
    while contador < len(nueva_lista):
        palabra_actual = nueva_lista[contador]
        if palabra_actual== word:
            return contador + indice
        contador += 1
    return -1


def index_of_empty(list):
    contador = 0
    while contador < len(lista):
        elemento_actual = lista[contador]
        if elemento_actual == "":
            return contador
        contador += 1
    return -1


def index_of(word, list):
    contador = 0
    while contador < len(lista):
        if word == lista[contador]:
            return contador
        contador += 1
    return -1


def put(word, list):
    contador = 0
    for elemento in lista:
        if elemento == "":
            lista[contador] = word
            return contador
        contador += 1    
    return -1

def remove(word, list):
    palabras_eliminadas = 0
    for indice in range (len(lista)):
        if lista[indice] == word:
            lista[indice] = ""
            palabras_eliminadas += 1
    return palabras_eliminadas



