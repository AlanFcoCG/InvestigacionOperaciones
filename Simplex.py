matrix=[[1, -180, -90, 0, 0, 0], [0, 1, 0, 1, 0, 6], [0, 0, 1, 0, 1, 4]]

for i in range(len(matrix)):
    print(matrix[i])

def detectar_pivote(mref):
    minimo=0
    for i in range(len(mref[0])):
        c=mref[0][i]
        if c < minimo and (c<0 or c!=0):
            minimo=c
            pivote=i

    return pivote

def detectar_piv_fila(columna, matrix):
    radio=[]
    minimo=0
    piv_fil=0
    for pos_fila in range(len((matrix))):
        try:
            radio.append(float((matrix[pos_fila][-1])/(matrix[pos_fila][int(columna)])))
        except ZeroDivisionError:
            radio.append(0)
        print(radio[pos_fila])
        if radio[pos_fila] > minimo and pos_fila > 0:
            minimo=radio[pos_fila]
            piv_fil=pos_fila
    print("El radio minimo es: " + str(minimo))
    return piv_fil


#--------------------MAIN-------------------------

col_piv=detectar_pivote(matrix)
fil_piv=detectar_piv_fila(col_piv, matrix)
print("Columna privote: "+str(col_piv)+" Fila pivote: "+str(fil_piv))
