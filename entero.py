class prime_class:    
    global valor
    global op
    valor=int(raw_input("Ingrese un numero: "))
    
    
    #if (resultado != ):
    def is_prime(self):
        if valor <= 2:   
            return "es numero primo"
        else:
            cont = 0
            cont = cont + 1
            while cont < 3:
                if valor % cont != 0:
                    cont = cont + 1
                    return "es numero primo"
                else:
                    cont = cont + 1    
            return "no es numero primo" 
    resultado=is_prime(valor)
    print resultado
