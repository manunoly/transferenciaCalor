__author__ = 'manuel'


## Constante
SteffanBoltzmann = 0.0000000567

## variables de la pared
k = 1.63  # conductividad termica
cpp = 1090.0    # calor especifico pared especifico
densp = 2400.0
alphap = .82 ## absortividad
ep  = .95  ## emisividad
diff  = 6.23 * 10 ** -7  ## difusividad terminca  -- calculable
x = .12 # distancia entre las divisiones de la pared
# numero de biot a
a = (alphap * 60) / (0.015 ** 2) # conducti -- calculable
estabilidad  = (diff * 3600) / x # estabilidad  -- calculable
l  = 2.0  ## altura de la pared


# propiedades pared - aire
ufpa = .0 #viscocidad cinematica de la pared-aire
denspa = .0 ## densidad
condpa =.0
cppa = .0 # calor especifico pared aire
betapa =.0
deltapa =.0
prpa =.0
vfpa = .0
grpa = .0
rapa = .0
nusseltpa = .0
hw = .0
tmpa = .0 #temp media


#propiedades del vidrio
T = 0.84 #transmitancia
absortancia = .0 # absortancia
ev = 0.8 #Emisividad
alphav = 0.006


#propiedades vidrio - aire

ufva = .0 #viscocidad cinematica del vidrio-aire
densva = .0 # densidad del vidrio aire
condva = .0 # conductividad del vidrio aire
cpva = .0  # calor especifico
betava =.0
deltava =.0
prva =.0
vfva  = .0
grva = .0
rava = .0
nusseltva  = .0
hg = .0
tmva = .0 #temp media


#aberturas de ingreso y salida del aire
ancho = .0
largo = .0

#variables del clima
Ta = .0 #Temp Ambiental
Ta = 295.0
velocidadViento = 1.0 #V
radicacion = .0 #rad vertical -- ver con geovanna como se calcula la radiacion vertical, se debe ir variando segun las horas del dia.


# Temperatura del cielo
Ts = .0
Ts = 0.0552 * (Ta ** 1.5)



#temp pared del extremo inicial, puede ser una constante o toca investigar como hacer su calculo inicial. la T1 va variando con el tiempo.
T1 = .0
#valor inicial
T1 = 308.0
#temp pared otro extremo puede ser una constante o toca investigar como hacer su calculo inicial. la T15 va variando con el tiempo. 308 valor inicial luego se calcula
T15 = 308.0
#valor cuando varia la temperatura, seria en la proxima hora.
#T15 = ((((k / x)*(T1 - T15[0])) - (hwind * (T15[0] - Ta[0]))))

To = Ta
Tg = Ta
rangoTg = 2
incremento = 0.2
while Tg < Tg + rangoTg:
    Tf = Tg
    while To < To + 1:
        To = To + incremento
        while Tf < To:
            print(Tf)
            Tf = Tf + incremento
    Tg = Tg + incremento

exit()

#variables a calcular que van a ir variando.
Tg = .0 #temp del vidrio
Tg = 296.0
Tf = .0 #temp del fluido
Tf = 304.0
To = .0 #temp inicial de la pared
To = 308.0

# Calculo de Sw calor de radiacion
sw = T * alphap * radicacion
# Calcular Sg calor de radiacion en el vidrio
Sg = .0
# la radiacion va variando a cada hora segun condiciones climaticas
sg = alphav * radicacion
# hwind coeficiente de transferencia de calor por conveccion del viento externo
hwind = .0
# la velocidad del viento va variando a cada hora segun condiciones climaticas
hwind = 5.7 + (3.8 * velocidadViento)
#la Tg Tf To temp deben ir variando dentro de las siguientes formulas
#con el valor inicial de las var anteriores calcular
# hrwg  coeficiente de radiacion entre la pared y el vidrio
# hrgs  coeficiente de radiacion entre el vidrio y el ambiente
# hrws  coeficiente de radiacion entre la pared y el ambiente
hrwg = SteffanBoltzmann * (((Tg ** 2 + To ** 2)* (Tg + To))/((1/ev)+(1/ep)-1))
hrgs = (SteffanBoltzmann * ev) * (Tg + Ts) * (Tg ** 2 + Ts ** 2)
hrws = (SteffanBoltzmann * ep) * (T15 + Ts) * (T15 ** 2 + Ts ** 2)

#vamos a calcular las propiedades del vidrio - aire
tmva = (Tg + Tf)/2
ufva = (1.846 + (0.00472 * (tmva - 300))) * 10 ** -5
densva = (1.1614 - (0.00353 * (tmva - 300)))
condva = (0.0263 + (0.000074 * (tmva - 300)))
cpva = (1.007 + (0.00004 * (tmva -300))) * 10 ** 3
betava = 1.0/tmva

deltava = abs(Tg - Tf)
prva = (ufva * cpva) / condva
vfva = ufva / densva
grva = (9.8 * betava * deltava * (l ** 3)) / (vfva ** 2)
rava = prva * grva
if rava < 10 ** 9:
    nusseltva = 0.68 + (0.67 * rava ** (1.0/4)) / (1 + (0.492 / prva) ** (9.0 / 16)) ** (4.0 /9)
else:
    nusseltva = (0.825 + (0.387 * (rava ** (1/6))) / (1 + (0.492 / prva) **(9.0/16)) **(8.0 /27)) ** 2

hg = (nusseltva * condva) / l

# vamos a calcular las propiedades de la pared - aire
tmpa = (Tf + To) / 2
ufpa = (1.846 + (0.00472 * (tmpa - 300))) * 10 ** -5
denspa = (1.1614 - (0.00353 * (tmpa - 300)))
condpa = (0.0263 + (0.000074 * (tmpa - 300)))
cppa = (1.007 + (0.00004 * (tmpa -300))) * 10 ** 3
betapa = 1.0/tmpa
deltapa = abs(To - Tf)
prpa = (ufpa * cppa) / condpa
vfpa = ufpa / denspa
grpa = (9.8 * betapa * deltapa * (l ** 3)) / (vfpa ** 2)
rapa = prpa * grpa
if rapa < 10 ** 9:
    nusseltpa = 0.68 + (0.67 * rapa ** (1.0/4)) / (1 + (0.492 / prpa) ** (9.0 / 16)) ** (4.0 /9)
else:
    nusseltpa = (0.825 + (0.387 * (rapa ** (1/6))) / (1 + (0.492 / prpa) **(9.0/16)) **(8.0 /27)) ** 2

hw = (nusseltpa * condpa) / l

#hay q variar To, Tg, Tf para que aproximado de 0
# variar To, comenzar con temp ambiental y variar 50 mas
# variar Tg comenzar con temp ambiental  y variar 2 mas
# variar Tf comenzar con Tg y terminar con To pq siempre tiene q estar en este rango.
aproximado = sg + (hg * (Tf - Tg)) + (hrwg * (To - Tg)) - (hwind * (Tg - Ta)) - (hrgs * (Tg - Ts))
exit()
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