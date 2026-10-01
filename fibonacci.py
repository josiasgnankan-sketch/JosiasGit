def fibanocci(n):
    a,b=0,1
    for i in range(n):
             print(a)
             a,b=b,a+b
            
    
if __name__=="__main__":
    while True:
      nb=input("Entrez un nombre pour calculer la suite de Fibonacci : ")

      if nb.isdigit():
         nb=int(nb)
         print(f" les {nb} termes de fibanocci  sont :")
         fibanocci(nb)

      else:
        print("Veullez entrer un nombre entier")
