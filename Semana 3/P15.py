#Problema 15

def bisiesto(num):
     if num % 4 == 0 and (num % 100 != 0 or num % 400 == 0):
        print("es bisiesto")
     else:
        print("no es bisiesto")

bisiesto(2020) 
