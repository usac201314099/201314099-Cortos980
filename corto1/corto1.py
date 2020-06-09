#corto 1 
#carne 201314099 ----099
#congetura 3n+1
numero=0

Collatz = [] #lista para guardar la secuencias

def Secuencia(numero): #funcion para hacer la secuencia
    N=int(numero)
    print(N)
    while N > 1:  
        if N%2 ==0: #comprueva se es par
            Collatz.append(N) #guarda en la lista
            N=N/2 #el siguiente sera la mitad
        else:
            Collatz.append(N) # si no es para 
            N=3*N+1
    Collatz.append(1) #agraga la ailtima cifra 1       
    print(Collatz)  

Secuencia(6)
    
    
    

    