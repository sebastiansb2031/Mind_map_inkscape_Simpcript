import inkex
import random
import numpy as np

Mascara1=np.array(Mascara1)
Mascara1_txt=np.array(Mascara1_txt)
Mascaracon=np.array(Mascaracon)
Hipervinculo1=np.array(Hipervinculo1)
#svg_root.namedview.set('showgrid', 'true')
''' Coordenadas de la elipse'''
#Escala=1/1.35

'''Coordenas de la elipse'''
entrada='Esternocleidomastoideo'
ancho_fuente=1*mm
largo_msj=len(entrada)*ancho_fuente
largo_ttl=(len(Mascara1_txt[0])*3*ancho_fuente)   #Longitud del mensaje completo en pixeles
ancho_elipse=largo_msj 
ancho_elipse_ttl=largo_ttl
largo_elipse=ancho_fuente*4
largo_elipse_ttl=ancho_fuente*4*3
radio_min0=ancho_elipse_ttl
pcentralx0=296/2
pcentraly0=210/2
radioxinicial=ancho_elipse/2
radioyinicial=largo_elipse

radio_min=2*2*max(radioxinicial,radioyinicial)
Tamaño=np.bincount(Mascara1)
globals()["Escalag"]=1
globals()["MedidaU"]=Tamaño[len(Tamaño)-1]*max(ancho_elipse,largo_elipse)/(2*pi)+radio_min*((len(Tamaño)))+ancho_elipse_ttl+radio_min0
#Escala=pcentralx/globals()["MedidaU"]
Escala=1

#globals()["pcentralx"]=globals()["Escalag"]*globals()["MedidaU"]*296/210
#globals()["pcentraly"]=globals()["Escalag"]*globals()["MedidaU"]
globals()["pcentralx"]=globals()["Escalag"]*globals()["MedidaU"]
globals()["pcentraly"]=globals()["Escalag"]*globals()["MedidaU"]

'''Coordenas de la elipse'''##########################################################################
entrada='Esternocleidomastoideo'
ancho_fuente=1*mm*Escala
largo_msj=len(entrada)*ancho_fuente
largo_ttl=(len(Mascara1_txt[0])*3*ancho_fuente)   #Longitud del mensaje completo en pixeles
ancho_elipse=largo_msj 
ancho_elipse_ttl=largo_ttl
largo_elipse=ancho_fuente*4
largo_elipse_ttl=ancho_fuente*4*3
##############################################################################################
radio_min=2*2*Escala*max(radioxinicial,radioyinicial)
Tamaño=np.bincount(Mascara1)
Colorespastel={'Rojo1':'#F2D7D5'}
Colorespastel2 ={'Rojo1' : '#E6B0AA', 'Rojo2' : '#F5B7B1', 'Morado1' : '#D7BDE2' , 'Morado2' : '#D2B4DE','Azul1' : '#A9CCE3' , 'Azul2' : '#AED6F1','Verde_azul1' : '#A3E4D7' , 'Verde_azul2' : '#A2D9CE','Verde1' : '#A9DFBF' , 'Verde2' : '#ABEBC6','Amarillo1' : '#F9E79F' , 'Amarillo2' : '#FAD7A0','Naranja1' : '#F5CBA7' , 'Naranja2' : '#EDBB99','Blanco1' : '#F7F9F9' , 'Blanco2' : '#E5E7E9','Gris1' : '#D5DBDB' , 'Gris2' : '#CCD1D1','Negro1' : '#AEB6BF' , 'Negro2' : '#ABB2B9'}
Colorespastel1 ={'Rojo1' : '#E6B0AA', 'Morado1' : '#D7BDE2' ,'Azul1' : '#A9CCE3'  ,'Verde1' : '#A9DFBF' ,'Amarillo1' : '#F9E79F' ,'Naranja1' : '#F5CBA7 ' ,'Gris1' : '#D5DBDB'  }
#1mm=3.78px (Si es milimetros multiplicar por 3.78)
#1pt=1.3333pt
color_e_ttl=random.choice(list(Colorespastel1.values()))



def angulos_limite(Mascara1,jerarquia,num):
 conta=0
 for i in range(len(Mascara1)):
  if Mascara1[i]==jerarquia:
   conta=conta+1
   if conta==num+1:
    i_actual=i
 conta2=0
 for i in range(i_actual):
  if Mascara1[i]==2:
   conta2=conta2+1
 angulon= (conta2-1)*(360/(np.bincount(Mascara1)[2]))*pi/180
 return angulon



def crear_matriz (matriz,Escala_radio):
 solape=0
 Tamaño=np.bincount(matriz)
 for k in range(len(Tamaño)-2) :
  
  q=Tamaño[k+1]
  qf=Tamaño[k+2]
  radio_min0=ancho_elipse_ttl
  radio_min=2*2*max(ancho_elipse/2,largo_elipse)
  if k<=3:
   radio=((q)*(max(ancho_elipse,largo_elipse))/(2*pi)+radio_min*((2*k))+radio_min0)*Escala_radio
   radiof=((qf)*(max(ancho_elipse,largo_elipse))/(2*pi)+radio_min*((2*(k)))+radio_min0)*Escala_radio
  else:
   radio=((q)*(max(ancho_elipse,largo_elipse))/(2*pi)+radio_min*((1*(k))))*Escala_radio
   radiof=((qf)*(max(ancho_elipse,largo_elipse))/(2*pi)+radio_min*((1*(k)+1)))*Escala_radio
  if k>3:
   #if k==4:
    #radioant=((Tamaño[k+1])*(max(ancho_elipse,largo_elipse))/(2*pi)+radio_min*((2*(k-1)))+radio_min0)*Escala_radio
    #while radio<radioant+2*radio_min:
     #radio=radio+radio_min
   while radiof<radio+3*radio_min:
    radiof=radiof+(2*(k)-3)*radio_min
  radiof2=((qf)*(max(ancho_elipse,largo_elipse))/(2*pi)+radio_min*(k)+radio_min0)*Escala_radio
  qh=2*pi*radio/(max(ancho_elipse,largo_elipse))
  qhf=2*pi*radiof/(max(ancho_elipse,largo_elipse))
  ang_actual=0
  nactual=0
  nactual2=0
  aux1=0
  if k==len(Tamaño)-1:
   globals()["Radiomax"]=radiof
  if k>0:
   resh=360/(qh)
   res=360/(q)
   resf=360/(qhf)
   for i in range(q): #num. de elementos de la jerarquia anterior
    if k==1:
     ang_actual=(i)*res*pi/180
    else:
     ang_actual=(i)
    for n in range(globals()["Nelementos"+str(k+1)+str(i)]): #numero de elementos jerarquia superior de cada elementos de jerarquia anterior
     if n%2==0:
      globals()["Angulo"+str(k+2)+str(nactual+n)]=round((angulos_limite(Mascara1,k+2,n+nactual)+resf*(n)*pi/180)/(resf*pi/180))*(resf*pi/180)
      if nactual>0: 
       while globals()["Angulo"+str(k+2)+str(nactual+n)]-globals()["Angulo"+str(k+2)+str(nactual+n-1)]<(resf*pi/(180*2)):
        globals()["Angulo"+str(k+2)+str(nactual+n)]=round((angulos_limite(Mascara1,k+2,n+nactual)+resf*(n+aux1)*pi/180)/(resf*pi/180))*(resf*pi/180)
        aux1=aux1+1
        if globals()["Angulo"+str(k+2)+str(nactual+n)]+(resf*pi)/180>(angulos_limite(Mascara1,k+2,n+nactual)+((360/(Tamaño[2]))*pi)/(180)):
         solape=1   
      aux1=0   
      globals()["Centrox"+str(k+2)+str(nactual+n)]=(radiof)*cos(globals()["Angulo"+str(k+2)+str(nactual+n)])+pcentralx
      globals()["Centroy"+str(k+2)+str(nactual+n)]=(radiof)*sin(globals()["Angulo"+str(k+2)+str(nactual+n)])+pcentraly
      globals()["Color"+str(k+2)+str(nactual+n)]=random.choice(list(
      Colorespastel1.values()))
     else:
      globals()["Angulo"+str(k+2)+str(nactual+n)]=round((angulos_limite(Mascara1,k+2,n+nactual)+resf*(n)*pi/180)/(resf*pi/180))*(resf*pi/180)
      
      if nactual>0: 
       while globals()["Angulo"+str(k+2)+str(nactual+n)]-globals()["Angulo"+str(k+2)+str(nactual+n-1)]<(resf*pi/(180*2)):
        globals()["Angulo"+str(k+2)+str(nactual+n)]=round(( angulos_limite(Mascara1,k+2,n+nactual)+resf*(n+aux1)*pi/180)/(resf*pi/180))*(resf*pi/180)
        aux1=aux1+1
        if globals()["Angulo"+str(k+2)+str(nactual+n)]+(resf*pi)/180>(angulos_limite(Mascara1,k+2,n+nactual)+((360/(Tamaño[2]))*pi)/(180)):
         solape=1   
      aux1=0   
      globals()["Centrox"+str(k+2)+str(nactual+n)]=(radiof)*cos(globals()["Angulo"+str(k+2)+str(nactual+n)])+pcentralx
      globals()["Centroy"+str(k+2)+str(nactual+n)]=(radiof)*sin(globals()["Angulo"+str(k+2)+str(nactual+n)])+pcentraly
      globals()["Color"+str(k+2)+str(nactual+n)]=random.choice(list(Colorespastel1.values()))
   
    
    nactual=nactual+globals()["Nelementos"+str(k+1)+str(i)] 
    nactual2=nactual2+int(globals()["Nelementos"+str(k+1)+str(i)]/2)+(globals()["Nelementos"+str(k+1)+str(i)]%2)
  else:
   #res=360/(qf+qf%2)
   res=360/(qf)
   for i in range(qf):
     globals()["Angulo"+str(2)+str(i)]=res*i*pi/180
     globals()["Centrox"+str(2)+str(i)]=(radiof2)*cos(ang_actual+res*i*pi/180)+pcentralx
     globals()["Centroy"+str(2)+str(i)]=( radiof2)*sin(ang_actual+res*i*pi/180)+pcentraly
     globals()["Color"+str(2)+str(i)]=random.choice(list(Colorespastel1.values()))
 return solape  
    
def prevenir_solape(Mascara1):
 while crear_matriz(Mascara1,globals()["Escalag"])>0:
  globals()["Escalag"]=globals()["Escalag"]+0.1
  globals()["pcentralx"]=globals()["Escalag"]*globals()["MedidaU"]
  globals()["pcentraly"]=globals()["Escalag"]*globals()["MedidaU"] 

def crear_lineas(matriz):
 Tamaño=np.bincount(matriz)
 
 for k in range(len(Tamaño)-2) :
  q=Tamaño[k+1]
  qf=Tamaño[k+2]
  nactual=0
  if k>0:   
   for i in range(q):   
    for n in range(globals()["Nelementos"+str(k+1)+str(i)]):         
       line((globals()["Centrox"+str(k+2)+str(nactual+n)],  globals()["Centroy"+str(k+2)+str(nactual+n)]), ( globals()["Centrox"+str(k+1)+str(i)],  globals()["Centroy"+str(k+1)+str(i)]), stroke=globals()["Color"+str(k+1)+str(i)],stroke_width=2*mm)   
    nactual=nactual+globals()["Nelementos"+str(k+1)+str(i)]   
  else:
   for i in range(qf):
      line((globals()["Centrox"+str(2)+str(i)],  globals()["Centroy"+str(2)+str(i)]), (pcentralx, pcentraly), stroke=color_e_ttl,stroke_width=2*mm) 
   

def crear_elipses(matriz):
 Tamaño=np.bincount(matriz)
 
 for k in range(len(Tamaño)-2) :
  q=Tamaño[k+1]
  qf=Tamaño[k+2]
  nactual=0
  if k>0:   
   for i in range(q):   
    for n in range(globals()["Nelementos"+str(k+1)+str(i)]):         
      if Mascaracon[np.where(Mascara1==k+2)[0][nactual+n]]=="1" :
       globals()["e" + str(nactual+n+1)+str(k+2)]=ellipse((globals()["Centrox"+str(k+2)+str(nactual+n)],globals()["Centroy"+str(k+2)+str(nactual+n)]), (ancho_elipse/2, largo_elipse), stroke_width= 0,fill=globals()["Color"+str(k+2)+str(nactual+n)] )   
      else:
       globals()["e" + str(nactual+n+1)+str(k+2)]=ellipse((globals()["Centrox"+str(k+2)+str(nactual+n)],globals()["Centroy"+str(k+2)+str(nactual+n)]), (ancho_elipse/2, largo_elipse), stroke_width= 0,fill='#FFFFFF' )
    nactual=nactual+globals()["Nelementos"+str(k+1)+str(i)]   
  else:
   for i in range(qf):
     if Mascaracon[np.where(Mascara1==k+2)[0][i]]=="1" :
      globals()["e" + str(i+1)+str(k+2)]=ellipse(( globals()["Centrox"+str(2)+str(i)],globals()["Centroy"+str(2)+str(i)]), (ancho_elipse/2, largo_elipse), stroke_width= 0,fill=globals()["Color"+str(2)+str(i)] )
     else:
      globals()["e" + str(i+1)+str(k+2)]=ellipse(( globals()["Centrox"+str(2)+str(i)],globals()["Centroy"+str(2)+str(i)]), (ancho_elipse/2, largo_elipse), stroke_width= 0,fill='#000000' )
     #connector(globals()["e" + str(i+1)+str(k+2)], e0, ctype='polyline',stroke='#FF0000', stroke_width=1*Escala*mm) Conector que ya valio verga        
   
def crear_angulos(matriz): ##Funcion que 
 Tamaño=np.bincount(matriz)
 matrizres=[]
 matrizang=[]
 for i in range(2,len(Tamaño),1):  ##Vectores de posicion de jerarquías y resoluciones de ángulos
  matrizres.append(360/(Tamaño[i]+Tamaño[i]%2))
  globals()["conta"+str(i)]=0
  globals()["pos"+str(i)]=np.where(matriz==i)[0]
 for i in range(2,len(Tamaño)-1,1):
  globals()["Nelementosmax"+str(i)]=0
  for j in range(len(globals()["pos"+str(i)])):
   if j<len(globals()["pos"+str(i)])-1:
    globals()["Nelementos"+str(i)+str(j)]=len(globals()["pos"+str(i+1)][np.where((globals()["pos"+str(i+1)]>globals()["pos"+str(i)][j]) & (globals()["pos"+str(i+1)]<globals()["pos"+str(i)][j+1]))[0]])
   else:
    globals()["Nelementos"+str(i)+str(j)]=len(globals()["pos"+str(i+1)][np.where((globals()["pos"+str(i+1)]>globals()["pos"+str(i)][j]))[0]])
 matriz=np.zeros(len(Mascara1)) 
    
def Escribir_texto(matriz):
 Tamaño=np.bincount(matriz)
 for i in range(2,len(Tamaño),1):
  for j in range(Tamaño[i]):
   globals()["Texto"+str(i)+str(j)]=text(Mascara1_txt[np.where(Mascara1==i)[0][j]], (globals()["Centrox"+str(i)+str(j)]-len(Mascara1_txt[np.where(Mascara1==i)[0][j]])*ancho_fuente/2, globals()["Centroy"+str(i)+str(j)]),  font_size=2*mm*Escala)
    

def Escribir_hipervinculos(matriz):
 Tamaño=np.bincount(matriz)
 if Hipervinculo1[0]!="nulo":
  hyperlink(e0, str(Hipervinculo1[0]), title='Ver imagen') 
 for i in range(2,len(Tamaño),1):
  for j in range(Tamaño[i]):
   if Hipervinculo1[np.where(Mascara1==i)[0][j]]!="nulo":  
    hyperlink(globals()["e" + str(j+1)+str(i)], str(Hipervinculo1[np.where(Mascara1==i)[0][j]]), title='Ver imagen')
crear_angulos(Mascara1)
prevenir_solape(Mascara1)

#image('https://media.inkscape.org/static/images/inkscape-logo.png', (0, 0), embed=False)

#rect((0, 0), (2*pcentralx, 2*pcentraly),fill='#FDFDE5',stroke_width=1*mm)
#rect((0, 0), (2*pcentralx, 2*pcentraly),fill='#FFFFFF',stroke_width=1*mm)
rect((0, 0), (2*globals()["pcentralx"], 2*globals()["pcentraly"]),fill='#FFFFFF',stroke_width=1*mm)
crear_lineas(Mascara1)
crear_elipses(Mascara1)
e0=ellipse((pcentralx, pcentraly), (ancho_elipse_ttl, largo_elipse_ttl), stroke_width=0,fill=color_e_ttl)
Escribir_hipervinculos(Mascara1)
Titulo=text(Mascara1_txt[0], (pcentralx-largo_ttl/2,pcentraly+ancho_fuente),  font_size=6*mm*Escala)
Titulo_doc=text(Mascara1_txt[0], (pcentralx-largo_ttl*pcentralx/(pcentralx0), 3.2*3*ancho_fuente*pcentralx/pcentralx0),fill=color_e_ttl, stroke='#000000', stroke_width=0*mm, font_size=6*2*mm*pcentralx/pcentralx0)
Escribir_texto(Mascara1)



