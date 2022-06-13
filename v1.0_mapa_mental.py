import inkex
import numpy as np
''' Coordenadas de la elipse'''
radio_elipse_x=7.5
radio_elipse_y=5
'''Coordenas de la elipse'''
entrada='Esternocleidomastoideo'
ancho_fuente=3*pt
ancho_linea=0.625*mm
largo_msj=(len(entrada)*ancho_fuente)   #Longitud del mensaje completo en pixeles
ancho_elipse=2*ancho_linea+largo_msj+2*2*ancho_fuente
largo_elipse=ancho_fuente*8
pcentralx=700
pcentraly=500
#1mm=3.78px (Si es milimetros multiplicar por 3.78)
#1pt=1.3333pt
#Crea una elipse

#t11=text(entrada, (150-largo_msj-ancho_fuente , 200+ancho_fuente),  font_size='3pt')
#e11=ellipse((150, 200), (ancho_elipse, largo_elipse/2), stroke_width= ancho_linea)
#e2=ellipse((width/2, height/2), (radio_elipse_x*mm, radio_elipse_y*mm),  stroke_width=0.625*mm)


#connector(e11, e2, ctype='polyline', curve=10)
M_objetos = [[1, 1, 1, 1], 
    [1, 1, 1, 1],
    [1, 1, 1, 1 ]]
radioxinicial=ancho_elipse/2
radioyinicial=largo_elipse

Solapamiento=0
def add_j1(elipses,bifurcaciones,jerarquias):
 e0=ellipse((pcentralx, pcentraly), (radioxinicial, radioyinicial), stroke_width= ancho_linea)
 #print(len(M_objetos[0]))
 for k in range(jerarquias) :
  q=elipses*bifurcaciones**k
  radio=(q)*(max(ancho_elipse,largo_elipse)+2*ancho_linea)/(2*pi)
  radio_min=2*max(radioxinicial,radioyinicial) 
  radioextra=0
  Solapamiento=0 
  for i in range(0,q+q%2,2):
   res=360/(q+q%2)
   globals()["e" + str(i+1)+str(k+1)]=ellipse(((radio+radio_min)*cos(res*i*pi/180)+pcentralx,( radio+radio_min)*sin(res*i*pi/180)+pcentraly), (ancho_elipse/2, largo_elipse), stroke_width= ancho_linea ) 
  # connector(e+str(i+1)+str"", e12 , ctype='orthogonal', curve=10)
   if i+1<q:
    globals()["e" + str(i+2)+str(k+1)]=ellipse(((radio+radio_min)*cos(res*(i+1)*pi/180)+pcentralx,(radio+radio_min)*sin(res*(i+1)*pi/180)+pcentraly), (ancho_elipse/2, largo_elipse), stroke_width= ancho_linea )
    #x=np.linspace(-1*(ancho_elipse) ,ancho_elipse, 200)
   # if k>1:
    # connector(globals()["e" + str(i+1)+str(k+1)], globals()["e" + str(i+1)+str(k+1)] , ctype='orthogonal', curve=10)
   coordx1=((k+1)*radio+radio_min)*np.cos(res*i*pi/180)+pcentralx
   coordx2=((k+1)*radio+radio_min)*np.cos(res*(i+1)*pi/180)+pcentralx
   coordy1=((k+1)*radio+radio_min)*np.sin(res*i*pi/180)+pcentraly
   coordy2=((k+1)*radio+radio_min)*np.sin(res*(i+1)*pi/180)+pcentraly
   x1r=coordx1+ancho_elipse/2+ancho_linea
   x1l=coordx1-ancho_elipse/2-ancho_linea
   x2r=coordx2+ancho_elipse/2+ancho_linea
   x2l=coordx2-ancho_elipse/2-ancho_linea
   y1r=coordy1+largo_elipse+ancho_linea
   y1l=coordy1-largo_elipse-ancho_linea
   y2r=coordy2+largo_elipse+ancho_linea
   y2l=coordy2-largo_elipse-ancho_linea


###Calculando la raíz cuadrada
   x=np.linspace(-7.5,7.5,200)
   y1p=np.sqrt(abs((radioyinicial** 2)*(1-((x-coordx1)/radioxinicial)** 2)))+coordy1
   y1n=(-1)*np.sqrt(abs((radioyinicial** 2)*(1-((x-coordx1)/radioxinicial)** 2)))+coordy1
   g1p=np.sqrt(abs((radioyinicial** 2)*(1-((x-coordx2)/radioxinicial)** 2)))+coordy2
   g1n=(-1)*np.sqrt(abs((radioyinicial** 2)*(1-((x-coordx2)/radioxinicial)** 2)))+coordy2
   #print(y1p)
   for j in range(len(x)) :
     if y1p[j]==g1p[j] or  y1p[j]==g1n[j] or y1n[j]==g1p[j]or  y1n[j]==g1n[j] :
       print("alv")
#############################################################
   if abs(x1l-x2r)<abs(x1r-x2l):  #Nuevo elipse aparece por la izquierda si se cumple
    if x1l<x2r  :
     Solapamiento=1
     print("Solape izquierda en radio"+str(k+1)+" y circulo"+str(i+1) )
   else:
    if x2l<x1r :
     Solapamiento=1
     print("Solape derecha en radio"+str(k+1)+" y circulo"+str(i+1) )    #Nuevo globo entra por la derecha
   if abs(y1r-y2l)>abs(y1l-y2r):
    if y1r<y2l:
     Solapamiento=1
     print("Solape arriba en radio"+str(k+1)+" y circulo"+str(i+1) ) #El siguiente elipse comienza por arriba del anterior si se cumple               
   else: #EL siguiente elipse aparace abajo
    if y2r<y1l:
      Solapamiento=1
      print("Solape abajo en radio"+str(k+1)+" y circulo"+str(i+1) )
  if Solapamiento==1:
   for c in range(1,q+1):
    # globals()["e"+str(c)+str(k+1)].remove()
     print("Hay solape")
       
   #  Solapamiento=0
 





''' 
  for i in range(0,q+q%2,2):
   res=360/(q+q%2)
   globals()["e" + str(i+1)]=ellipse((2*radio*cos(res*i*pi/180)+pcentralx,2*radio*sin(res*i*pi/180)+pcentraly), (ancho_elipse/2, largo_elipse), stroke_width= ancho_linea )

   if i+1<q:
    globals()["e" + str(i+2)]=ellipse((2*radio*cos(res*(i+1)*pi/180)+pcentralx,2*radio*sin(res*(i+1)*pi/180)+pcentraly), (ancho_elipse/2, largo_elipse), stroke_width= ancho_linea )
'''
  
  #x=np.linspace(-7.5,7.5,200)

  #y1p=np.sqrt(abs((radioyinicial** 2)*(1-((x-coordx1)/radioxinicial)** 2)))+coordy1
  #g1p=np.sqrt(abs((radioyinicial** 2)*(1-((x-coordx2)/radioxinicial)** 2)))+coordy2

    #for k in range(len(x)) :
     #if y1p[k]==g1p[k] :
      # print("alv")



'''''
e1=ellipse((150, 200), (radio_elipse_x*mm, radio_elipse_y*mm),stroke_width=0.625*mm )
e2=ellipse((width/2, height/2), (radio_elipse_x*mm, radio_elipse_y*mm),  stroke_width=0.625*mm)
te2=text(entrada, (150-radio_elipse_x*mm + 3 , 200),  font_size='3pt')
#e3=ellipse((0, 0), (te2.width, te2.height),stroke_width=0.625 )
print(len(Entrada))	
'''

''' Intento mas o menos fallido de elipsoides en coordenadas polares
#i=0
#while i<10
 # coord_matriz=Input("Ingrese hasta la coordenada de la matriz de jerarquía  que desea entrar  x1 x2 x3 x4 .... xn"+ str(i))
  #Transformamos la entrada string en los parámetros de coordenada del mapa (int)
 # for k in range (1 3 1):
  #  globals()["d" + str(k)]=int(coord_matriz[-1+i])
  for b in range(1,4):
   for a in range(0, 360,int(36/b) ):
    x =b*100*cos(a*pi/180) 
    y =b*100*sin(a*pi/180)
    tr = inkex.Transform()
    tr.add_translate(x, y)
    clone(e2, transform=tr)
    for i in range(10):
      globals()["Elip" + str(i)]= ellipse((i*20, i*20), (radio_elipse_x*mm, radio_elipse_y*mm),  stroke_width=0.625*mm)


  #globals()["In" + str(i)]=Input("Ingrese la entrada "+ str(i))
  #globals()["In" + str(i)]=Input("Ingrese la entrada "+ str(i))

'''

#t11=text(entrada, (150-largo_msj-ancho_fuente , 200+ancho_fuente),  font_size='3pt')
#e11=ellipse((150, 200), (ancho_elipse, largo_elipse/2), stroke_width= ancho_linea)
#e2=ellipse((width/2, height/2), (radio_elipse_x*mm, radio_elipse_y*mm),  stroke_width=0.625*mm)


#connector(e11, e2, ctype='polyline', curve=10)

##############################################################
# Use Simple Inkscape Scripting to draw concentric circles #
##############################################################

##for i in range(10, 0, -1):
##    circle((150, 200),100*i)
          

##############################################################
# Use Simple Inkscape Scripting to draw concentric ellipses. #
##############################################################
'''
for b in range(1,4,1):
 for a in range(0, 360,int(36/b) ):
    x =b*100*cos(a*pi/180) 
    y =b*100*sin(a*pi/180)
    tr = inkex.Transform()
    tr.add_translate(x, y)
    clone(e2, transform=tr)
'''

''' Crear objetos o variables por index for
for i in range(10):
  globals()["Elip" + str(i)]= ellipse((i*20, i*20), (radio_elipse_x*mm, radio_elipse_y*mm),  stroke_width=0.625*mm)

Elip5.remove()
Elip2.remove()
'''


'''Multiples entradas de datos
for i in range(3):
  globals()["In" + str(i)]=Input("Ingrese la entrada "+str(i))
  
for i in range(3, 0, -1):
  print("Su ingreso"+ str(i)+ "fue"+ globals()["In"+str(i)])
'''
def crear_conexiones(q,p,k):
 for i in range(q):
  connector(e0, globals()["e" + str(i+1)+"1"], ctype='polyline', curve=10)
 for j in range(k):
  g=(i+1)*p**j
  for l in range(g):
   for b in range(p):
    connector(globals()["e" + str(l+1)+str(j+1)], globals()["e" + str(p*l+b+1)+str(j+2)], ctype='polyline', curve=10)
  # connector(globals()["e" + str(l+1)+str(j+1)], globals()["e" + str(2*l+2)+str(j+2)], ctype='polyline', curve=10)
   
e0=ellipse((pcentralx, pcentraly), (radioxinicial, radioyinicial), stroke_width= ancho_linea)
add_j1(20,1,3)
crear_conexiones(20,1,2)
#add_j1(30,1,1)



