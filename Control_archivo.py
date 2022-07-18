import numpy as np
import array
import math
##############################################Función que permite rellanar con ceros los codigos de los mapas##############
def poner_ceros (maximo,entrada):
 Nuevod=""
 Digitosm=len(str(maximo)) ##Cantidad de digitos determinante del formato
 Digitose=len(str(entrada)) ##Cantidad de digitos del dato particular 
 Dif=Digitosm-Digitose  ###Dif siempre será un número entero mayor a cero
 if Digitose<Digitosm:
  for i in range(Dif):
   Nuevod=str(Nuevod)+str(0)
 Nuevod=str(Nuevod)+str(entrada)
 return Nuevod
##########################################################################################################################
##############################################Función que permite rellanar con ceros a la derecha los codigos de los mapas##############
def poner_ceros_der (maximo,entrada,matriz):
 Nuevod=""
 Digitosm=len(str(maximo)) ##Cantidad de digitos determinante del formato
 Digitose=len(str(entrada)) ##Cantidad de digitos del dato particular 
 Dif=Digitosm-Digitose  ###Dif siempre será un número entero mayor a cero
 if Digitose<Digitosm:
  for i in range(Dif):
   Nuevod=str(Nuevod)+str(0)  
 return Nuevod
##########################################################################################################################
################Funcion que halla la posicion de jerarquia anterior########################################
def Encontrar_anterior(matriz,i_actual):
 aux=1
 aux2=i_actual-1
 while aux==1: 
  if matriz[i_actual]-matriz[aux2]==1:
   aux=0
   return aux2
  else:
   aux2=aux2-1


######################################################################################################################
##################Funcion que pone todos los elementos del array con el numero de digitos del digito mayor##########
def completar_digitos(matriz_original,matriz_transformada):
 matriz_transformada2=matriz_transformada
 maximo=(len(np.bincount(matriz_original))-1)*(2*(len(str(np.max(np.bincount(matriz_original)))))+len(str(len(np.bincount(matriz_original)))))
 for i in range(len(matriz_original)):
  if len(str(matriz_transformada[i]))<maximo:
   matriz_transformada[i]=matriz_transformada[i]+str(0)*(maximo-len(str(matriz_transformada[i])))
 return matriz_transformada2  
#############################################################################################################################
###################################Funcion que intercambia ambas matrices#####################################################
def intercambiar_matrices(matriz1,matriz2):
 matriz1c=[]
 matriz2c=[]
 alv=[]
 for i in range(len(matriz1)):
  matriz1c.append(int(matriz1[i]))  
 for i in range(len(matriz1)):
  for j in range(len(matriz1)):
   if matriz2[i]==matriz1c[j]:
    matriz2c.append(j)
    j=len(matriz1)  
 return matriz2c


#################################################################################################################


def organizar(Mascara1):
#organizar(Mascara1)
 Tamaño=np.bincount(Mascara1)
 matrizres=[]
 matrizang=[]
 
 for i in range(1,len(Tamaño),1):  ##Vectores de posicion de jerarquías y resoluciones de ángulos
  matrizres.append(360/(Tamaño[i]+Tamaño[i]%2))
  globals()["conta"+str(i)]=0
  globals()["pos"+str(i)]=np.where(np.array(Mascara1)==i)[0]
 for i in range(1,len(Tamaño)-1,1):
  globals()["Nelementosmax"+str(i)]=0
  for j in range(len(globals()["pos"+str(i)])):
   if j<len(globals()["pos"+str(i)])-1:
     globals()["Nelementos"+str(i)+str(j)]=len(globals()["pos"+str(i+1)][np.where((globals()["pos"+str(i+1)]>globals()["pos"+str(i)][j]) & (globals()["pos"+str(i+1)]<globals()["pos"+str(i)][j+1]))[0]])
   else:
     globals()["Nelementos"+str(i)+str(j)]=len(globals()["pos"+str(i+1)][np.where((globals()["pos"+str(i+1)]>globals()["pos"+str(i)][j]))[0]])
 for i in range(1,len(Tamaño),1):   
   for j in range(len(globals()["pos"+str(i)])):                     
     if j<len(globals()["pos"+str(i)])-1:
      globals()["Bloque"+str(i)+str(j)]=Mascara1[np.where(np.array(Mascara1)==i)[0][j]:np.where(np.array(Mascara1)==i)[0][j+1]]
     else:
      globals()["Bloque"+str(i)+str(j)]=Mascara1[np.where(np.array(Mascara1)==i)[0][j]:len(Mascara1)-1]
     
 
 globals()["M1T"]=Mascara1
 
 
 
 for i in range(1,len(np.bincount(Mascara1)),1):
  globals()["conta"+str(i)]=0
  
 #globals()["M1T"]=np.array(Mascara1)
 globals()["M1T"]=[]
 for i in range(len(Mascara1)):
  if Mascara1[i]<3:
   #globals()["M1T"][i]=int(str(1)+poner_ceros(len(np.bincount(Mascara1)),Mascara1[i])+poner_ceros(int(np.max(np.bincount(Mascara1))),int(str(np.max(np.bincount(Mascara1))-int(globals()["Nelementos"+str(Mascara1[i])+str(globals()["conta"+str(Mascara1[i])])]))))+str(poner_ceros(int(np.max(np.bincount(Mascara1))),globals()["conta"+str(Mascara1[i])]))) 
    globals()["M1T"].append(str(poner_ceros(len(np.bincount(Mascara1)),Mascara1[i])+poner_ceros(int(np.max(np.bincount(Mascara1))),int(str(np.max(np.bincount(Mascara1))-int(globals()["Nelementos"+str(Mascara1[i])+str(globals()["conta"+str(Mascara1[i])])]))))+str(poner_ceros(int(np.max(np.bincount(Mascara1))),globals()["conta"+str(Mascara1[i])]))) )
  if Mascara1[i]>2 and Mascara1[i]<len(np.bincount(Mascara1))-1:
  #str(globals()["M1T"][Encontrar_anterior(Mascara1,i)])
   #globals()["M1T"][i]=str(poner_ceros(len(np.bincount(Mascara1)),Mascara1[i])+poner_ceros(int(np.max(np.bincount(Mascara1))),int(str(np.max(np.bincount(Mascara1))-int(globals()["Nelementos"+str(Mascara1[i])+str(globals()["conta"+str(Mascara1[i])])]))))+str(poner_ceros(int(np.max(np.bincount(Mascara1))),globals()["conta"+str(Mascara1[i])])))
   globals()["M1T"].append(str(globals()["M1T"][Encontrar_anterior(Mascara1,i)])+str(poner_ceros(len(np.bincount(Mascara1)),Mascara1[i])+poner_ceros(int(np.max(np.bincount(Mascara1))),int(str(np.max(np.bincount(Mascara1))-int(globals()["Nelementos"+str(Mascara1[i])+str(globals()["conta"+str(Mascara1[i])])]))))+str(poner_ceros(int(np.max(np.bincount(Mascara1))),globals()["conta"+str(Mascara1[i])]))))
  if Mascara1[i]>=len(np.bincount(Mascara1))-1:
  
   globals()["M1T"].append(str(globals()["M1T"][Encontrar_anterior(Mascara1,i)])+str(poner_ceros(len(np.bincount(Mascara1)),Mascara1[i])+poner_ceros(int(np.max(np.bincount(Mascara1))),int(str(np.max(np.bincount(Mascara1))-int(globals()["Nelementos"+str(Mascara1[i]-1)+str(globals()["conta"+str(Mascara1[i])])]))))+str(poner_ceros(int(np.max(np.bincount(Mascara1))),globals()["conta"+str(Mascara1[i])]))))
  Nummaximo=(len(np.bincount(Mascara1))-1)*(2*(len(str(np.max(np.bincount(Mascara1)))))+len(str(len(np.bincount(Mascara1)))))
  globals()["conta"+str(Mascara1[i])]=int(globals()["conta"+str(Mascara1[i])])+1
 globals()["M1T"]=completar_digitos(Mascara1,globals()["M1T"])
 globals()["M2T"]=[]
 for i in range(len(Mascara1)):
  globals()["M2T"].append(int(globals()["M1T"][i]))
 longi=[]
 for i in range(len(Mascara1)):
  longi.append(len(str(globals()["M1T"][i])))
 globals()["M2T"].sort()    
 matriz_pos=intercambiar_matrices(globals()["M1T"],globals()["M2T"])
 return matriz_pos

  
  
def guardar(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1):
 Mascara1c=[]
 Mascara1_txtc=[]
 Mascaraconc=[]
 Hipervinculo1c=[]
 matriz_pos=organizar(Mascara1)
 for i in range(len(Mascara1)):
  Mascara1c.append(Mascara1[int(matriz_pos[i])])
  Mascara1_txtc.append(Mascara1_txt[int(matriz_pos[i])])
  Mascaraconc.append(Mascaracon[int(matriz_pos[i])])
  Hipervinculo1c.append(Hipervinculo1[int(matriz_pos[i])])
 texto=open("modelo_v1.0_mapa_mental.py",'r')
 #cadena="Mascara1= "+str(Mascara1)+"\n"+"Mascara1_txt= "+str(Mascara1_txt)+"\n"+"Mascaracon= "+str(Mascaracon)+"\n"+texto.read()
 cadena="Mascara1= "+str(Mascara1c)+"\n"+"Mascara1_txt= "+str(Mascara1_txtc)+"\n"+"Mascaracon= "+str(Mascaraconc)+"\n"+"Hipervinculo1= "+str(Hipervinculo1c)+"\n"+texto.read()
 texto2=open("v1.0_mapa_mental.py",'w')
 texto2.write(cadena)
 texto.close()
 texto2.close()
 
  
def crear_matriz():
  #globals()["posaux"]=0
  globals()["Atajo"]=0
  posaux=0
  c=input("1:Crear un nuevo mapa 2:Modificar un mapa existente q :para salir g:guardar mapa: :")
  if c=="1":
    #Mascara1=[int(1)]
    #Mascara1_txt=[""]
    #Hipervinculo1=["nulo"]
    #Mascaracon=[1]
    Mascara1=[1,2,3]
    Mascara1_txt=["Titulo","Subtitulo1","Subtitulo2"]
    Hipervinculo1=["nulo","nulo","nulo"]
    Mascaracon=[1,1,1]
    Mascaracon_aux=Mascaracon
    titulo1=str(input("Escriba el titulo del mapa mental:  "))
    Mascara1_txt_aux=Mascara1_txt
    Mascara1_txt[0]=titulo1
    Mascara1_txt_aux[0]=str("1")+str("1")+str(titulo1)
    guardar(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1)  
    editando=1
  if c=="2":
    arch=input("Indique el nombre del archivo,debe estar en el mismo directorio    :")
    with open(arch+".txt","r") as textoo:
     lines = textoo.readlines()
     textoo.close()
    Mascara1=lines[0].split()
    for i in range(len(Mascara1)):
     Mascara1[i]=int(Mascara1[i])
    #Mascara1=np.array(Mascara1) 
    Mascara1_txt=lines[1].split()
    for i in range(len(Mascara1_txt)):
     for j in range(len(Mascara1_txt[i])):
      if Mascara1_txt[i][j]=='_':
       Mascara1_txt[i]=str(Mascara1_txt[i][:j])+" "+str(Mascara1_txt[i][j+1:])
    Mascaracon=lines[2].split()
    Mascaracon_aux=Mascaracon
    Hipervinculo1=lines[3].split()
    Mascara1_txt_aux=lines[1].split()
    guardar(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1)
    for i in range(len(Mascara1_txt)):
     Mascara1_txt_aux[i]=str(Mascaracon[i])+str(Mascara1[i])+Mascara1_txt[i]
    guardar(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1)
  editando=1
  while editando==1:
     
   c0=input(str(Mascara1_txt_aux)+"\n"+"\n"+"Esta es la mascara actual"+"\n"+"Este es el término actual: "+str(Mascara1_txt_aux[posaux])+"\n"+"Ingrese el indice y la palabra o q :para salir g:guardar mapa hh:Crear hipervinculo :")
   for i in range(len(Mascara1_txt)):
      if Mascara1_txt_aux[i]==c0:
       posaux=i
       i=len(Mascara1_txt)+1
   if c0=="g":
    c0g=input("Indique el nombre del archivo:  ")
    cadena=""
    for i in range(len(Mascara1)):
     cadena=cadena+str(Mascara1[i])+" "
    cadena=cadena+"\n"
    for i in range(len(Mascara1)):
     cadena=cadena+Mascara1_txt[i]+" "
    cadena=cadena+"\n"
    for i in range(len(Mascaracon)):
     cadena=cadena+str(Mascaracon[i])+" "
    cadena=cadena+"\n"
    for i in range(len(Hipervinculo1)):
     cadena=cadena+str(Hipervinculo1[i])+" "
    cadena=cadena+"\n"
    texton=open( c0g+".txt",'w')
    texton.write(cadena)
    texton.close()
   if c0=="q":
    editando=0
   
   for i in range(len(Mascara1_txt)):
     if Mascara1_txt_aux[i]==c0:
      #globals()["posaux"]=i
      posaux=i
      i=len(Mascara1_txt)+1
   #c0aux=input("d o cd:Borrar cc o  c:Renombrar cnw o nw:Nueva rama nueva jerarquia o hh:Hipervinculo:  ")
   if c0=="hh" :
    chh=input("Ingrese el link del hipervinculo:  ")
    #Hipervinculo1[globals()["posaux1"]]=str(chh)
    Hipervinculo1[posaux]=str(chh)
    guardar(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1)
   if c0=="d" :
    Mascara1_txt[posaux]=""
    Mascaracon[posaux]="1"
    guardar(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1)
    for i in range(len(Mascara1_txt)):
     Mascara1_txt_aux[i]=str(Mascaracon[i])+str(Mascara1[i])+Mascara1_txt[i]
    guardar(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1)
   if c0=="cd" :
    Mascara1_txt[posaux]=""
    Mascaracon[posaux]="0"
    for i in range(len(Mascara1_txt)):
     Mascara1_txt_aux[i]=str(Mascaracon[i])+str(Mascara1[i])+Mascara1_txt[i]
    guardar(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1)
   if c0=="c" :
    entradad=input("Ingrese el termino nuevo a reemplazar    :")
    Mascara1_txt[posaux]=entradad
    Mascara1_txt_aux[posaux]=str(Mascara1[posaux])+entradad
    Mascaracon[posaux]="1"
    for i in range(len(Mascara1_txt)):
     Mascara1_txt_aux[i]=str(Mascaracon[i])+str(Mascara1[i])+Mascara1_txt[i]
    guardar(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1) 
   if c0=="cc" :
    entradad=input("Ingrese el termino nuevo a reemplazar    :")
    Mascara1_txt[posaux]=entradad
    Mascara1_txt_aux[posaux]=str(Mascara1[posaux])+entradad
    Mascaracon[posaux]="0"
    for i in range(len(Mascara1_txt)):
     Mascara1_txt_aux[i]=str(Mascaracon[i])+str(Mascara1[i])+Mascara1_txt[i]
    guardar(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1)
   if c0=="nw":
    entradanw=input("Ingrese el nuevo termino a reemplazar     :")
    #Tamaño=np.bincount(Mascara1)
    Mascara1.append(Mascara1[len(Mascara1_txt)-1])
    Mascara1_txt.append(Mascara1_txt[len(Mascara1_txt)-1])
    Mascara1_txt_aux.append(Mascara1_txt[len(Mascara1_txt)-1])
    Mascaracon.append(Mascaracon[len(Mascaracon)-1])
    Hipervinculo1.append(Hipervinculo1[len(Hipervinculo1)-1])
    for i in range(len(Mascara1_txt[posaux:])-1):
     Mascara1[len(Mascara1)-1-i]=Mascara1[len(Mascara1)-2-i]
     Mascara1_txt[len(Mascara1)-1-i]=Mascara1_txt[len(Mascara1)-2-i]
     Mascara1_txt_aux[len(Mascara1)-1-i]=Mascara1_txt[len(Mascara1)-2-i] 
     Mascaracon[len(Mascara1)-1-i]=Mascaracon[len(Mascara1)-2-i]
     Hipervinculo1[len(Mascara1)-1-i]=Hipervinculo1[len(Mascara1)-2-i] 
    Mascara1[posaux+1]=int(Mascara1[posaux+1])+1
    Mascara1_txt[posaux+1]=entradanw
    Mascara1_txt_aux[posaux+1]=str(Mascara1[posaux+1])+entradanw
    Mascaracon[posaux+1]="1"
    Hipervinculo1[posaux+1]="nulo"
    for i in range(len(Mascara1_txt)):
     Mascara1_txt_aux[i]=str(Mascaracon[i])+str(Mascara1[i])+Mascara1_txt[i]
    guardar(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1)
    #globals()["posaux"]=globals()["posaux"]+1
    posaux=posaux+1 
   if c0=="cnw":
    entradanw=input("Ingrese el nuevo termino a reemplazar     :")
    #Tamaño=np.bincount(Mascara1)
    Mascara1.append(Mascara1[len(Mascara1_txt)-1])
    Mascara1_txt.append(Mascara1_txt[len(Mascara1_txt)-1])
    Mascara1_txt_aux.append(Mascara1_txt[len(Mascara1_txt)-1])
    Mascaracon.append(Mascaracon[len(Mascaracon)-1])
    Hipervinculo1.append(Hipervinculo1[len(Hipervinculo1)-1])
    for i in range(len(Mascara1_txt[posaux:])-1):
     Mascara1[len(Mascara1)-1-i]=Mascara1[len(Mascara1)-2-i]
     Mascara1_txt[len(Mascara1)-1-i]=Mascara1_txt[len(Mascara1)-2-i]
     Mascara1_txt_aux[len(Mascara1)-1-i]=Mascara1_txt[len(Mascara1)-2-i]
     Mascaracon[len(Mascara1)-1-i]=Mascaracon[len(Mascara1)-2-i]
     Hipervinculo1[len(Mascara1)-1-i]=Hipervinculo1[len(Mascara1)-2-i]
    Mascara1[posaux+1]=int(Mascara1[posaux+1])+1
    Mascara1_txt[posaux+1]=entradanw
    Mascara1_txt_aux[posaux+1]=str(Mascara1[posaux+1])+entradanw
    Mascaracon[posaux+1]="0"
    Hipervinculo1[posaux+1]="nulo"
    for i in range(len(Mascara1_txt)):
     Mascara1_txt_aux[i]=str(Mascaracon[i])+str(Mascara1[i])+Mascara1_txt[i]
    guardar(Mascara1,Mascara1_txt,Mascaracon,Hipervinculo1) 
    #globals()["posaux"]=globals()["posaux"]+1
    posaux=posaux+1
   if c0=="-1":
    posaux=posaux-1
crear_matriz()
