"""
La siguiente clase te permite sabe si el numero que ingresas es primo o no

Recordemos que un numero primo es aque que solo da enteros divisible entre el y 1 , es decir solo tiene 2 divisibles que den 0, si tiene uno más ya no se puede considerar primo.
"""


class prime_class:    
    global valor 
    global op
    valor=int(raw_input("Ingrese un numero: ")) #se ingresa el numero y se guarda en valor
    
    def is_prime(self):
        if valor <= 2:  #si el valor es igual o menor a 2 siempre sera un numero primo 
            return "es numero primo"
        else:
            cont = 0 #inicializamos contador
            cont = cont + 1
            while cont < 3: #mientras el contador sea menor a 3 sera un numero primo.
                if valor % cont != 0:
                    cont = cont + 1
                    return "es numero primo"
                else:
                    cont = cont + 1    
            return "no es numero primo" 
        
    resultado=is_prime(valor)
    print resultado
