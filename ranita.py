mapa= [
    ["X" , "I" , "X" , "X" , "X" , "X" , "X"],
    ["X" , " " , "X" , "X" , "T1" , " " , "X"],
    ["X" , " " , "T2" , "X" , " " , " " , "X"],
    ["X" , " " , " " , "X" , "B" , " " , "X"],
    ["X" , " " , " " , "X" , "T2" , " " , "X"],
    ["X" , "T1" , "B" , "X" , "X" , " " , "X"],
    ["X" , "X" , "X" , "X" , "X" , "S" , "X"],
]

x = 0
y = 0

print("La rana empieza en la posición (0,0)")
print((mapa[y])[x])
i = 0

while (mapa[y])[x] == " ":
    direccion = input("Selecciona la dirección en la que deseas moverte (ARRIBA, ABAJO, DERECHA, IZQUIERDA): ")
    
    if direccion == "ABAJO" or "ARRIBA" or "DERECHA" or "IZQUIERDA":
        print("Has seleccionado {}".format(direccion))
    
    if direccion == "ABAJO":
        x = x
        y = y + 1
    elif direccion == "ARRIBA":
        x = x
        y = y - 1
    elif direccion == "DERECHA":
        x = x - 1
        y = y 
    elif direccion == "IZQUIERDA":
        x = x + 1
        y = y 
    else:
        print("SOLO SE PUEDEN ELEGIR LAS OPCIONES DE DIRECCIÓN EXPLICADAS, ELIGE BIEN")
        print("\n")


    print("Estás en la casilla ({},{})".format(x,y))
    if (mapa[y])[x] == ' ':
        print("La casilla elegida NO es un muro, puede continuar en el laberinto")
    elif (mapa[y])[x] == 'S':
        print("Has llegado a la salida del laberibnto. ¡HAS GANADO!")
        break
    else:
        print("La casilla es un muro \nReinicia el programa para seguir jugando")

#if __name__ == '__main__':
    #first_multiple_input = input().rstrip().split()
    #n = int(first_multiple_input[0])
    #m = int(first_multiple_input[1])
    #k = int(first_multiple_input[2])

#for n in range(n):
    #row = input()


#for k_itr in range(k):
    #second_multiple_input = input().rstrip().split()
    #i1 = int(second_multiple_input[0])
    #j1 = int(second_multiple_input[1])
    #i2 = int(second_multiple_input[2])
    #j2 = int(second_multiple_input[3])