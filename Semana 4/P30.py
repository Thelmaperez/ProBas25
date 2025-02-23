#Problema 30 
#Implementar funciones recursivas

def rec(num):
    print("incial → %i"%(num))
    
    if num > 1:
        num = num * rec(num -1)
    
    print("Final → %i",(num))
    return(num)
result = rec(5)
print(result)