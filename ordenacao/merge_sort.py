
def intercala(inicio, meio, fim, lista):
    i = inicio
    j = meio
    lista_ordenada = []
    while i < meio and j < fim:
        if lista[i] < lista[j]:
            lista_ordenada.append(lista[i])
            i = i+1
        else:
            lista_ordenada.append(lista[j])
            j = j+1
    # pq i == meio ou j == fim
    # vamos pegar todos os elementos da primeira metade da lista
    while i < meio:
        lista_ordenada.append(lista[i])
        i = i+1

    while j < fim:
        lista_ordenada.append(lista[j])
        j = j+1
    # novidade da aula de hoje
    for m in range(inicio, fim):
        lista[m] = lista_ordenada[m-inicio]


def mergeSort(inicio, fim, lista):
    if inicio < fim - 1:
        meio = (inicio+fim)//2
        mergeSort(inicio, meio, lista)
        mergeSort(meio, fim, lista)
        intercala(inicio, meio, fim, lista)
        

# main: principal
if __name__ == '__main__':
    valores = [29, 10, 14, 37, 13, 1]
    mergeSort(0, len(valores), valores)
    print(valores)








    
    
    
    
    
    
    #mergeSort(0, 5, valores)
    #print(valores)
    # valores = [1,3,6,7,0,8,11,12]
    # inicio = 0
    # fim = len(valores)
    # meio = (inicio+fim)//2
    # intercala(inicio, meio, fim, valores)
    # print(valores)