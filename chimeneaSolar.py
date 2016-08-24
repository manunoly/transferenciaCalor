__author__ = 'manuel'



def ecuacion1(Tg, Tf):
    return 1

def ecuacion2(H1,H2):
    return 2

## Constante
SteffanBoltzmann = 0.0000000567

## variables de la pared
k = .0  ## conductividad termica
Cp = .0 ## calor especifico
dens = .0 ## densidad
alpha = .0 ## absortividad
E  = .0  ## emisividad
diff  = .0  ## difusividad terminca  -- calculable

## numero de biot
A  = .0 ## conducti -- calculable
Estabilidad  = .0 ## estabilidad  -- calculable
L  = .0  ## altura de la pared

#propiedades del vidrio
T = .0 #transmitancia
absortancia = .0 # absortancia
E = .0 #Emisividad

#aberturas de ingreso y salida del aire
ancho = .0
largo = .0

#variables del clima
tempAmb = .0 #Ta
velocidadViento = .0 #V
radicacion = .0 #rad vertical -- ver con geovanna como se calcula la radiacion vertical

#variables a calcular que van a ir variando.
Tg = .0 #temp del vidrio
Tf = .0 #temp del fluido
To = .0 #temp inicial de la pared

# Calculo de Sw calor de radiacion
Sw = .0
# Calcular Sg calor de radiacion en el vidrio
Sg = .0
# hwind coeficiente de transferencia de calor por conveccion del viento externo
hwind = .0

#la Tg Tf To temp deben ir variando dentro de las siguientes formulas
#con el valor inicial de las var anteriores calcular
# hrwg  coeficiente de radiacion entre la pared y el vidrio
# hrgs  coeficiente de radiacion entre el vidrio y el ambiente
# hrws  coeficiente de radiacion entre la pared y el ambiente

# hw    coeficiente de conveccion de la pared y el aire
# hg    coeficiente de conveccion del vidrio y el aire
    # para calcular hg hay q calcular primero la Tm temperetura media y luego las propiedades del aire y luego se calcula el Ra(Raile)
    # Si Ra tiene un valor se utiliza formula X si otro valor se utiliza formula y
    # se calcula Nu (nusel)
    #con este Nu es que se calcula finalmente hg y hw

#luego utilizar la ecuacion de Tg (valance de energia en el vidrio) que es la que se debe igualar variando las temperaturas,  debo quedarme con la temperatura que logre igualar

#toca calcular por cada hora del dia, para la proxima hora se utiliza To y solo se varian Tf y Tg lo cual daria en calcular en nuevos valores para Tf y Tg y seguir para la proxima hora

#definir los puntos de division de la pared, Delta x no puede ser mayor que 0.25, si deseo lo puedo dividir en menos puntos de lo que en principio puede darme la cantidad de ranuras siempre que el espacio no sea mayor de 0.25


print(SteffanBoltzmann)