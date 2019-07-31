def numeros_de_entradas(numeros):
        num = ordenar_numeros(numeros)
        i = 0
        contador= []
        while (i <= num):

            contador += [i]
            i += 1
        e = 0
        binarioList=[]
        while (e < len(contador)):
              binarioList.append(int(binario(contador[e])))
              e+=1
                
        return binarioList

def numeros_en_orden(numeros):
        num = ordenar_numeros(numeros)
        i = 0
        contador= []
        while (i <= num):
            contador += [i]
            i += 1
        return contador

def pren_apag(numeros):
        numero = numeros_en_orden(numeros)
        w = 0
        res = []
        for j in numero:
                res.append(0)
        for e in numeros:
                for i in numero:
                        if( e == i):
                                res[i] = 1    
        return res

def binario(n):
    if n == 0:
        return "0"
    else:
        return binaux(n, "")

def binaux(n,res):
    if n == 0:
        return invertir(res)
    else:
        res+=str(n%2)
        return binaux(n//2, res)
    
def invertir(string):
    if len(string) == 1:
        return string
    else:
        return invaux(string, "", len(string)-1)

def invaux(string, res, pos):
    if pos < 0:
        return res
    else:
        res += string[pos]
        pos-=1
        return invaux(string, res, pos)

def ordenar_numeros(lista):
        i = 0
        maximo = -1
        while(i < len(lista)):
            numero = lista[i]
            if(maximo < numero ):
                maximo = numero
            i += 1
        return int(maximo)

def convertir(numeros):
        res= pren_apag(numeros)
        i= 0
        nr= []
        while i < len(res):
                lis= numeros_en_orden(numeros)
                if res[i] == 1:
                        n= lis[i]
                        nr.append(binario(n))
                i+= 1
        return nr

                

# Este sabe cuantos unos tiene en los binarios puede probarlo con lista [12,23,34,40]
def contar_cantidad_unos(numeros):
        num = convertir(numeros)
        i = 0
        lista = []
        contador = 0
        while i < len(num):
                binario = num[i]
                binar = str(binario)
                contador = 0
                j=0
                while j < len(binar):
                        
                        if binar[j] == '1':
                                contador += 1  
                        j+=1
                lista.append(contador)        
                i+=1

        return lista

def agrupar(numeros):
        res= []
        nums= convertir(numeros)
        cant= contar_cantidad_unos(numeros)
        i= 0
        cero = []
        uno= []
        dos= []
        tres= []
        cuatro= []
        cinco= []
        seis= []
        siete= []
        ocho= []
        nueve= []
        diez= []
        while i < len(cant):
                valor= cant[i]
                n= nums[i]
                if valor == 0:
                        cero.append(n)
                elif valor == 1:
                        uno.append(n)
                elif valor == 2:
                        dos.append(n)
                elif valor == 3:
                         tres.append(n)
                elif valor == 4:
                         cuatro.append(n)
                elif valor == 5:
                         cinco.append(n)
                elif valor == 6:
                         seis.append(n)
                elif valor == 7:
                         siete.append(n)
                elif valor == 8:
                         ocho.append(n)
                elif valor == 9:
                         nueve.append(n)
                elif valor == 10:
                         diez.append(n)
                i+= 1
        if cero != []:
                print("Cero"'\n')
                print(cero)
                res += [0]
        if uno != []:
                print("Uno"'\n')
                print(uno)
                res += [1]
        if dos != []:
                 print("DOS"'\n')
                 print(dos)
                 res += [2]
        if tres != []:
                print("Tres"'\n')
                print(tres)
                res += [3]
        if cuatro != []:
                print("Cuatro"'\n')
                print(cuatro)
                res += [4]
        if cinco != []:
                print("Cinco"'\n')
                print(cinco)
                res += [5]
        if seis != []:
                print("Seis"'\n')
                print(seis)
                res += [6]
        if siete != []:
                print("Siete"'\n')
                print(siete)
                res += [7]
        if ocho != []:
                print("Ocho"'\n')
                print(ocho)
                res += [8]
        if nueve != []:
                print("Nueve"'\n')
                print(nueve)
                res += [9]
        if diez != []:
                print("Dies"'\n')
                print(diez)
                res += [10]
        j= 0


        
        '''
        print(cero), print(uno), print(dos), print(tres),  print(cuatro),  print(cinco),  print(seis),  print(siete),  print(ocho),  print(nueve), print(diez)       
        '''


        
'''
def main():

    lista = []
    continuar = True
    while continuar:
        print("\n"+"\n"+"\n"+"Bienvenidos"+"\n"+"Quine–McCluskey"+"\n"+"\n"+"Seleccione una de las siguientes opcciones:"+"\n"+"\n"+"1.Instrucciones de uso"+"\n"+"2.Crear circuito Quine–McCluskey"+"\n"+"3.salir"+"\n"+"\n")    
        accion = str(input("Ingrese su opcion: "))
        if accion == '1':
                print("\n"+"\n"+"\n"+"INSTRUCCIONES DE USO"+"\n"+"\n"+"\n"+"aqui tenemos q poner como se utiliza"+"\n"+"\n"+"\n")
        if accion == '2':
                
                valor = int(input("\n"+"\n"+"Ingrese la lista:  "))
                        
                numeros_de_entradas(valor)
                
        if accion == '3':
                continuar = False
            
if __name__=="__main__":
    main()
'''
