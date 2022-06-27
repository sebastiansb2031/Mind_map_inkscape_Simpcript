import inkex
import random
import numpy as np

Mascara1=np.array(Mascara1)
Mascara1_txt=np.array(Mascara1_txt)
Mascaracon=np.array(Mascaracon)
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

pcentralx0=296/2
pcentraly0=210/2
radioxinicial=ancho_elipse/2
radioyinicial=largo_elipse

radio_min=2*2*max(radioxinicial,radioyinicial)
Tamaño=np.bincount(Mascara1)
#globals()["MedidaU"]=max(Tamaño[len(Tamaño)-1]*max(ancho_elipse,largo_elipse)/(2*pi)+radio_min*(len(Tamaño)-1),pcentralx)
globals()["MedidaU"]=Tamaño[len(Tamaño)-1]*max(ancho_elipse,largo_elipse)/(2*pi)+radio_min*(len(Tamaño)-1)+ancho_elipse_ttl
#Escala=pcentralx/globals()["MedidaU"]
Escala=1
pcentralx=globals()["MedidaU"]
pcentraly=globals()["MedidaU"]*210/296

'''Coordenas de la elipse'''
entrada='Esternocleidomastoideo'
ancho_fuente=1*mm*Escala
largo_msj=len(entrada)*ancho_fuente
largo_ttl=(len(Mascara1_txt[0])*3*ancho_fuente)   #Longitud del mensaje completo en pixeles
ancho_elipse=largo_msj 
ancho_elipse_ttl=largo_ttl
largo_elipse=ancho_fuente*4
largo_elipse_ttl=ancho_fuente*4*3

#radioxinicial=ancho_elipse*Escala/2
#radioyinicial=largo_elipse*Escala

radio_min=2*2*Escala*max(radioxinicial,radioyinicial)
Tamaño=np.bincount(Mascara1)

#radio_elipse_x=pcentralx/1000+pcentraly/10000
#radio_elipse_y=pcentraly/1000
Colorespastel={'Rojo1':'#F2D7D5'}
Colorespastel2 ={'Rojo1' : '#E6B0AA', 'Rojo2' : '#F5B7B1', 'Morado1' : '#D7BDE2' , 'Morado2' : '#D2B4DE','Azul1' : '#A9CCE3' , 'Azul2' : '#AED6F1','Verde_azul1' : '#A3E4D7' , 'Verde_azul2' : '#A2D9CE','Verde1' : '#A9DFBF' , 'Verde2' : '#ABEBC6','Amarillo1' : '#F9E79F' , 'Amarillo2' : '#FAD7A0','Naranja1' : '#F5CBA7' , 'Naranja2' : '#EDBB99','Blanco1' : '#F7F9F9' , 'Blanco2' : '#E5E7E9','Gris1' : '#D5DBDB' , 'Gris2' : '#CCD1D1','Negro1' : '#AEB6BF' , 'Negro2' : '#ABB2B9'}
Colorespastel1 ={'Rojo1' : '#E6B0AA', 'Morado1' : '#D7BDE2' ,'Azul1' : '#A9CCE3'  ,'Verde1' : '#A9DFBF' ,'Amarillo1' : '#F9E79F' ,'Naranja1' : '#F5CBA7 ' ,'Gris1' : '#D5DBDB'  }
#print(random.choice(list(Colorespastel1.values())))
#colorindex=random.randomint(0,len(Colorespastel))
#1mm=3.78px (Si es milimetros multiplicar por 3.78)
#1pt=1.3333pt
color_e_ttl=random.choice(list(Colorespastel1.values()))

#Mascara2=np.array([1,2,3,4,5,5,3,3,4,5,5,2,3,3,3,2,3,3,3,4,5,6,5,6,6])

#svg_root.set('width', str(pcentralx*2)+'mm')
#svg_root.set('height', str(pcentraly*2)+'mm')
 
def crear_lineas (matriz):
 #e0=ellipse((pcentralx, pcentraly), (radioxinicial, radioyinicial), stroke_width= ancho_linea,fill='#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256)))
 Tamaño=np.bincount(matriz)
 #print(Tamaño)
 
 for k in range(len(Tamaño)-2) :
  q=Tamaño[k+1]
  qf=Tamaño[k+2]
  radio_min0=ancho_elipse_ttl
  radio_min=2*2*max(ancho_elipse/2,largo_elipse)
  radio=(q)*(max(ancho_elipse,largo_elipse))/(2*pi)+radio_min*(k+1)+radio_min0
  radiof=(qf)*(max(ancho_elipse,largo_elipse))/(2*pi)+radio_min*(2*k+2)+radio_min0
  radiof2=(qf)*(max(ancho_elipse,largo_elipse))/(2*pi)+radio_min*(2*k+2)+radio_min0
  qh=2*pi*radio/(max(ancho_elipse,largo_elipse))
  qhf=2*pi*radiof/(max(ancho_elipse,largo_elipse))
  ang_actual=0
  nactual=0
  aux1=0
  if k>0:
   resh=360/(qh+qh%2)
   res=360/(q+q%2)
   resf=360/(qhf+qhf%2)
   for i in range(q): #num. de elementos de la jerarquia anterior
    if k==1:
     ang_actual=(i)*res*pi/180
    else:
     ang_actual=(i)
    for n in range(globals()["Nelementos"+str(k+1)+str(i)]): #numero de elementos jerarquia superior de cada elementos de jerarquia anterior
     globals()["Angulo"+str(k+2)+str(nactual+n)]= round((globals()["Angulo"+str(k+1)+str(i)]+resf*(n)*pi/180)/(resf*pi/180))*(resf*pi/180)
     if nactual>0: 
      while globals()["Angulo"+str(k+2)+str(nactual+n)]-globals()["Angulo"+str(k+2)+str(nactual+n-1)]<(resf*pi/(180*2)):
       globals()["Angulo"+str(k+2)+str(nactual+n)]= round((globals()["Angulo"+str(k+1)+str(i)]+resf*(n+aux1)*pi/180)/(resf*pi/180))*(resf*pi/180)
       aux1=aux1+1
     aux1=0   
     globals()["Centrox"+str(k+2)+str(nactual+n)]=(radiof)*cos(globals()["Angulo"+str(k+2)+str(nactual+n)])+pcentralx
     globals()["Centroy"+str(k+2)+str(nactual+n)]=(radiof)*sin(globals()["Angulo"+str(k+2)+str(nactual+n)])+pcentraly
     globals()["Color"+str(k+2)+str(nactual+n)]=random.choice(list(Colorespastel1.values()))
     line((globals()["Centrox"+str(k+2)+str(nactual+n)],  globals()["Centroy"+str(k+2)+str(nactual+n)]), ( globals()["Centrox"+str(k+1)+str(i)],  globals()["Centroy"+str(k+1)+str(i)]), stroke=globals()["Color"+str(k+1)+str(i)],stroke_width=1*mm)
    nactual=nactual+globals()["Nelementos"+str(k+1)+str(i)]
  else:
   res=360/(qf+qf%2)
   for i in range(qf):
     globals()["Angulo"+str(2)+str(i)]=res*i*pi/180
     globals()["Centrox"+str(2)+str(i)]=(radiof2)*cos(ang_actual+res*i*pi/180)+pcentralx
     globals()["Centroy"+str(2)+str(i)]=( radiof2)*sin(ang_actual+res*i*pi/180)+pcentraly
     globals()["Color"+str(2)+str(i)]=random.choice(list(Colorespastel1.values()))
     line((globals()["Centrox"+str(2)+str(i)],  globals()["Centroy"+str(2)+str(i)]), (pcentralx, pcentraly), stroke=color_e_ttl,stroke_width=1*mm)  
   

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
   
def crear_angulos(matriz):
 #print(matriz)
 #print(len(matriz))
 Tamaño=np.bincount(matriz)
 matrizres=[]
 matrizang=[]
 for i in range(2,len(Tamaño),1):  ##Vectores de posicion de jerarquías y resoluciones de ángulos
  matrizres.append(360/(Tamaño[i]+Tamaño[i]%2))
  globals()["conta"+str(i)]=0
  #print("conta "+str(i))
  globals()["pos"+str(i)]=np.where(matriz==i)[0]
  #print(globals()["pos"+str(i)])
 #print(Tamaño[2:])
 #print(matrizres)
 for i in range(2,len(Tamaño)-1,1):
  globals()["Nelementosmax"+str(i)]=0
  for j in range(len(globals()["pos"+str(i)])):
   if j<len(globals()["pos"+str(i)])-1:
    globals()["Nelementos"+str(i)+str(j)]=len(globals()["pos"+str(i+1)][np.where((globals()["pos"+str(i+1)]>globals()["pos"+str(i)][j]) & (globals()["pos"+str(i+1)]<globals()["pos"+str(i)][j+1]))[0]])
   else:
    globals()["Nelementos"+str(i)+str(j)]=len(globals()["pos"+str(i+1)][np.where((globals()["pos"+str(i+1)]>globals()["pos"+str(i)][j]))[0]])
    #print("Nelementos"+str(i)+str(j+1))
    #print(globals()["Nelementos"+str(i)+str(j)])
   #globals()["Nelementosmax"+str(i)]=max(globals()["Nelementosmax"+str(i)],globals()["Nelementos"+str(i)+str(j)])  
  #print("max "+str(i)+str(globals()["Nelementosmax"+str(i)]))  
  
  
def Colores(matriz):
 Tamaño=np.bincount(matriz)
 for i in range(2,len(Tamaño),1):
  for j in range(Tamaño[i]):
   if Mascaracon[np.where(Mascara1==i)[0][j]]=="0":
    globals()["e"+str(j+1)+str(i)]=ellipse((globals()["Centrox"+str(i)+str(j)],globals()["Centroy"+str(i)+str(j)]), (ancho_elipse/2, largo_elipse), stroke_width= 0,fill='#FFFFFF')
    #globals()["e"+str(j+1)+str(i)].remove()
    #globals()["e"+str(j)+str(i)].fill="#FFFFFF"   
    
    
def Escribir_texto(matriz):
 Tamaño=np.bincount(matriz)
 for i in range(2,len(Tamaño),1):
  for j in range(Tamaño[i]):
   globals()["Texto"+str(i)+str(j)]=text(Mascara1_txt[np.where(Mascara1==i)[0][j]], (globals()["Centrox"+str(i)+str(j)]-len(Mascara1_txt[np.where(Mascara1==i)[0][j]])*ancho_fuente/2, globals()["Centroy"+str(i)+str(j)]),  font_size=2*mm*Escala)


rect((0, 0), (2*pcentralx, 2*pcentraly),fill='#FDFDE5',stroke_width=1*mm)
#image('https://media.inkscape.org/static/images/inkscape-logo.png', (0, 0), embed=False)


crear_angulos(Mascara1)
crear_lineas(Mascara1)
crear_elipses(Mascara1)
e0=ellipse((pcentralx, pcentraly), (ancho_elipse_ttl, largo_elipse_ttl), stroke_width=0,fill=color_e_ttl)
Titulo=text(Mascara1_txt[0], (pcentralx-largo_ttl/2,pcentraly+ancho_fuente),  font_size=6*mm*Escala)
Titulo_doc=text(Mascara1_txt[0], (pcentralx-largo_ttl*pcentralx/(pcentralx0), 3.2*3*ancho_fuente*pcentralx/pcentralx0),fill=color_e_ttl, stroke='#000000', stroke_width=0*mm, font_size=6*2*mm*pcentralx/pcentralx0)
Escribir_texto(Mascara1)

#svg_root.set('width', str(globals()["MedidaU"]*Escala*2)+'mm')
#svg_root.set('height', str(globals()["MedidaU"]*Escala*2*210/296)+'mm')



