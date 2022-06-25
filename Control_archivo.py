'''
a1=input("Ingrese el numero de elipses: ")
a2=input("Ingrese el numero de bifurcaciones: ")
a3=input("Ingrese el numero de jerarquias: ")'''
import numpy as np


#Mascara1_txt=["hola1"," hola2"," hola3"," hola4"," hola5"," hola6"," hola6"," hola6"," hola6"]
#for i in range(len(Mascara1_txt)):
 #Mascara1_txt[i]=str(Mascara1[i])+Mascara1_txt[i]
Mascaracon=[1, 1 ,0, 0, 0, 1, 1]
def guardar(Mascara1,Mascara1_txt,Mascaracon):
 texto=open("modelo_v1.0_mapa_mental.py",'r')
 cadena="Mascara1= "+str(Mascara1)+"\n"+"Mascara1_txt= "+str(Mascara1_txt)+"\n"+"Mascaracon= "+str(Mascaracon)+"\n"+texto.read()
 #cadena="\na3="+a3+"\na4=a3-1 \n"+texto.read()
 #cadena=texto.read()
 texto2=open("v1.0_mapa_mental.py",'w')
 texto2.write(cadena)
 #print(texto2.read())
 texto.close()
 texto2.close()

def crear_matriz():
  
  c=input("1:Crear un nuevo mapa 2:Modificar un mapa existente q :para salir g:guardar mapa: :")
  if c=="1":
    Mascara1=[int(1)]
    Mascara1_txt=[""]
    Mascaracon=[1]
    Mascaracon_aux=Mascaracon
    titulo1=str(input("Escriba el titulo del mapa mental:  "))
    Mascara1_txt_aux=Mascara1_txt
    Mascara1_txt=[titulo1]
    Mascara1_txt_aux=["1"+titulo1]
    guardar(Mascara1,Mascara1_txt,Mascaracon) 
    print(Mascara1)
    print(Mascara1_txt_aux)  
  if c=="2":
    #arch=input("Indique el nombre del archivo,debe estar en el mismo directorio    :")
    #textoo=open("holap.txt","r")
    #textoo2=textoo.readlines()
    with open('holap.txt',"r") as textoo:
     lines = textoo.readlines()
     textoo.close()
    #Mascara1_txt=[]
    #Mascara1=[] 
    Mascara1=lines[0].split()
    print("longitud "+str(Mascara1[1]))
    for i in range(len(Mascara1)):
     Mascara1[i]=int(Mascara1[i])
     #guardar()
    Mascara1_txt=lines[1].split()
    Mascaracon=lines[2].split()
    Mascaracon_aux=Mascaracon
    Mascara1_txt_aux=lines[1].split()
    print("longitud "+str(Mascara1_txt[1]))
    #for i in range(len(Mascara1)):
     #Mascara1_txt[i]=str(Mascara1_txt[i])
     #guardar()   
    #print(lines[1])
    
    guardar(Mascara1,Mascara1_txt,Mascaracon)
   
    for i in range(len(Mascara1_txt)):
     Mascara1_txt_aux[i]=str(Mascaracon[i])+str(Mascara1[i])+Mascara1_txt[i]
    print(Mascara1)
    print(Mascara1_txt)
    
    guardar(Mascara1,Mascara1_txt,Mascaracon)
    
  editando=1
  while editando==1:
     
   c0=input(str(Mascara1_txt_aux)+"Esta es la mascara actual,ingrese el indice y la palabra o q :para salir g:guardar mapa:")
   #c0=input("Esta es la mascara actual,ingrese el indice y la palabra o q :para salir g:guardar mapa:")
   if c0=="g":
    c0g=input("Indique el nombre del archivo:  ")
    cadena=""
    for i in range(len(Mascara1)):
     cadena=cadena+str(Mascara1[i])+" "
    cadena=cadena+"\n"
    for i in range(len(Mascara1)):
     cadena=cadena+Mascara1_txt[i]+" "
    cadena=cadena+"\n"
    texton=open( c0g+".txt",'w')
    texton.write(cadena)
    texton.close()
   if c0=="q":
    editando=0
   else:
    for i in range(len(Mascara1_txt)):
      if Mascara1_txt_aux[i]==c0:
       posaux=i
       i=len(Mascara1_txt)+1
    c0aux=input("d o cd:Borrar cc o  c:Renombrar cnw o nw:Nueva rama nueva jerarquia  :")
    if c0aux=="d" :
     Mascara1_txt[posaux]=""
     Mascaracon[posaux]="1"
     guardar(Mascara1,Mascara1_txt,Mascaracon)
     print(Mascara1_txt)
    if c0aux=="cd" :
     Mascara1_txt[posaux]=""
     Mascaracon[posaux]="0"
     guardar(Mascara1,Mascara1_txt,Mascaracon)
     print(Mascara1_txt)
    if c0aux=="c" :
     print(Mascara1_txt[posaux])
     entradad=input("Ingrese el termino nuevo a reemplazar    :")
     Mascara1_txt[posaux]=entradad
     Mascara1_txt_aux[posaux]=str(Mascara1[posaux])+entradad
     Mascaracon[posaux]="1"
     guardar(Mascara1,Mascara1_txt,Mascaracon)
     print(Mascara1_txt_aux) 
    if c0aux=="cc" :
     print(Mascara1_txt[posaux])
     entradad=input("Ingrese el termino nuevo a reemplazar    :")
     Mascara1_txt[posaux]=entradad
     Mascara1_txt_aux[posaux]=str(Mascara1[posaux])+entradad
     Mascaracon[posaux]="0"
     guardar(Mascara1,Mascara1_txt,Mascaracon)
     print(Mascara1_txt_aux)  
    if c0aux=="nw":
     entradanw=input("Ingrese el nuevo termino a reemplazar     :")
     #Tamaño=np.bincount(Mascara1)
     Mascara1.append(Mascara1[len(Mascara1_txt)-1])
     Mascara1_txt.append(Mascara1_txt[len(Mascara1_txt)-1])
     Mascara1_txt_aux.append(Mascara1_txt[len(Mascara1_txt)-1])
     Mascaracon.append(Mascaracon[len(Mascaracon)-1])
     for i in range(len(Mascara1_txt[posaux:])-1):
      Mascara1[len(Mascara1)-1-i]=Mascara1[len(Mascara1)-2-i]
      Mascara1_txt[len(Mascara1)-1-i]=Mascara1_txt[len(Mascara1)-2-i]
      Mascara1_txt_aux[len(Mascara1)-1-i]=Mascara1_txt[len(Mascara1)-2-i] 
      Mascaracon[len(Mascara1)-1-i]=Mascaracon[len(Mascara1)-2-i] 
     Mascara1[posaux+1]=int(Mascara1[posaux+1])+1
     Mascara1_txt[posaux+1]=entradanw
     Mascara1_txt_aux[posaux+1]=str(Mascara1[posaux+1])+entradanw
     Mascaracon[posaux+1]="1"
     guardar(Mascara1,Mascara1_txt,Mascaracon)
     print(Mascara1_txt_aux)
     
    if c0aux=="cnw":
     entradanw=input("Ingrese el nuevo termino a reemplazar     :")
     #Tamaño=np.bincount(Mascara1)
     Mascara1.append(Mascara1[len(Mascara1_txt)-1])
     Mascara1_txt.append(Mascara1_txt[len(Mascara1_txt)-1])
     Mascara1_txt_aux.append(Mascara1_txt[len(Mascara1_txt)-1])
     Mascaracon.append(Mascaracon[len(Mascaracon)-1])
     for i in range(len(Mascara1_txt[posaux:])-1):
      Mascara1[len(Mascara1)-1-i]=Mascara1[len(Mascara1)-2-i]
      Mascara1_txt[len(Mascara1)-1-i]=Mascara1_txt[len(Mascara1)-2-i]
      Mascara1_txt_aux[len(Mascara1)-1-i]=Mascara1_txt[len(Mascara1)-2-i]
      Mascaracon[len(Mascara1)-1-i]=Mascaracon[len(Mascara1)-2-i]
     Mascara1[posaux+1]=int(Mascara1[posaux+1])+1
     Mascara1_txt[posaux+1]=entradanw
     Mascara1_txt_aux[posaux+1]=str(Mascara1[posaux+1])+entradanw
     Mascaracon[posaux+1]="0"
     guardar(Mascara1,Mascara1_txt,Mascaracon)
     print(Mascara1_txt_aux) 
    
    '''
    if c0aux=="n" :
     entradan=input("Ingrese el nuevo termino a reemplazar     :")
      #Tamaño=np.bincount(Mascara1)
     Mascara1.append(Mascara1[len(Mascara1_txt)-1])
     Mascara1_txt.append(Mascara1_txt[len(Mascara1_txt)-1])
     Mascara1_txt_aux.append(Mascara1_txt[len(Mascara1_txt)-1])
     Mascaracon.append("1")
     for i in range(len(Mascara1_txt[posaux:])-1):
      Mascara1[len(Mascara1)-1-i]=Mascara1[len(Mascara1)-2-i]
      Mascara1_txt[len(Mascara1)-1-i]=Mascara1_txt[len(Mascara1)-2-i]
      Mascara1_txt_aux[len(Mascara1)-1-i]=Mascara1_txt[len(Mascara1)-2-i]
      Mascaracon[len(Mascara1)-1-i]=Mascaracon[len(Mascara1)-2-i]
     Mascara1[posaux+1]=Mascara1[posaux+1]
     Mascara1_txt[posaux+1]=entradan
     Mascara1_txt_aux[posaux+1]=str(Mascara1[posaux+1])+entradan
     Maux=Mascara1_txt[posaux]
     Mascara1_txt[posaux]=Mascara1_txt[posaux+1]
     Mascara1_txt[posaux+1]=Maux
     
     
     Maux=Mascaracon[posaux]
     Mascaracon[posaux]=Mascaracon[posaux+1]
     Mascaracon[posaux+1]=Maux
     
     guardar(Mascara1,Mascara1_txt,Mascaracon)
     print(Mascara1)
    if c0aux=="cn" :
     entradan=input("Ingrese el nuevo termino a reemplazar     :")
      #Tamaño=np.bincount(Mascara1)
     Mascara1.append(Mascara1[len(Mascara1_txt)-1])
     Mascara1_txt.append(Mascara1_txt[len(Mascara1_txt)-1])
     Mascara1_txt_aux.append(Mascara1_txt[len(Mascara1_txt)-1])
     Mascaracon_aux=Mascaracon
     Mascaracon.append("0")
     Mascaracon_aux.append("0")
     for i in range(len(Mascara1_txt[posaux:])-1):
      Mascara1[len(Mascara1)-1-i]=Mascara1[len(Mascara1)-2-i]
      Mascara1_txt[len(Mascara1)-1-i]=Mascara1_txt[len(Mascara1)-2-i]
      Mascara1_txt_aux[len(Mascara1)-1-i]=Mascara1_txt[len(Mascara1)-2-i]
      Mascaracon[len(Mascara1)-1-i]=Mascaracon[len(Mascara1)-2-i]
      Mascaracon_aux[len(Mascara1)-1-i]=Mascaracon[len(Mascara1)-2-i]
   
     Mascara1[posaux+1]=Mascara1[posaux+1]
     Mascara1_txt[posaux+1]=entradan
     Mascara1_txt_aux[posaux+1]=str(Mascara1[posaux+1])+entradan
     Maux=Mascara1_txt[posaux]
     Mascara1_txt[posaux]=Mascara1_txt[posaux+1]
     Mascara1_txt[posaux+1]=Maux
     
     
     Maux=Mascaracon[posaux]
     Mascaracon[posaux]=Mascaracon[posaux+1]
     Mascaracon[posaux+1]=Maux
     
     
     
     guardar(Mascara1,Mascara1_txt,Mascaracon)
     print(Mascara1) 
     '''
     #M_conceptos[int(c1)][]=[texto]





#b=0
#while b==0:

#texto.write("Hello from Python!")
#Mascara1=[1,2,3,4,5,5,5,5,5]
Mascaracon=[1, 1 ,0, 0, 0, 1,1]
crear_matriz()

#Mascara2=[1,2,3,4,5,5,3,3,4,5,5,2,3,3,3,2,3,3,3,4,5,6,5,6,6]
 #Mascara2_txt=np.zeros(len(Mascara2))


'''
import numpy as np
posicion=[1,1,1]
Mascara=np.array([1,2,3,4,5,5,3,3,4,5,5,2,3,3,3,2,3,3,3,4,5,6,5,6,6])
Tamaño=np.bincount(Mascara)
M= ""

#for i in range(len(posicion)):
 #M= M+"["+str(posicion[i])+"]"
 #globals()[str(Matriz)+str(M)]=0
#Matriz[posicion[0]][posicion[1]][posicion[2]]=0
print(Tamaño)
print()
'''
