__author__ = 'manuel'

import os
from xlrd import open_workbook
import math

book = open_workbook('/home/manuel/andreitaTest/juanpi/DatosClima.xlsx')
sheet = book.sheet_by_index(0)
datosExcel = []

for row in xrange(sheet.nrows):
#    datosExcel.append(sheet.row_values(row,0,4))
    datosExcel.append(sheet.row_values(row,0,4))
primeraFila = True
contenedor = []
contenedorCero = []
for datoExcel in datosExcel:
    if primeraFila:
        primeraFila = False
        continue
    else:
        print datoExcel
        Ta = datoExcel[1]
        v = datoExcel[3]
        H = datoExcel[2]
        alpha1 = 0.06
        trans = 0.84
        alpha2 = 0.95
        hi = 3.0
        esp = 0.05
        Kpared = 0.067
        g = 9.8
        Lw = 1.875
        z = 0.1
        Ew = 0.95
        Eg = 0.9
        mejorTgP = 100
        mejorTfP = 100
        mejorTwP = 100
        mejorFilaP = []
        mejorFilaN = []

        Aber=0.1
        W=0.8
        Aberi=0.1
        Wi=0.8

        Ao=Aber*W
        Ai=Aberi*Wi
        Ar=Ao/Ai
        valorF = 1000
        a = 0
        Tg = 298
        while Tg < 373:
            Tw = 298
            while Tw < 373:
                Tf = 293
                while Tf < 373:
                    if (Tg <> Ta and Tf < Tg and Tf < Tw and Tf > Ta):
                        a = a+1

                        Tfo=(Tf-(0.25*Ta))/(0.75)
                        po=(1.1614-0.00353*(Tfo-300))
                        Ts=0.0552*(Ta**1.5)
                        hrs = (0.0000000567*Eg*(Tg+Ts)*(Tg**2 + Ts**2)*(Tg-Ts))/(Tg-Ta)
                        h=5.7+3.8*v
                        Ut=h+hrs
                        hrwg = (0.0000000567*(Tg**2+Tw**2)*(Tg+Tw))/((1/Eg)+(1/Ew)-1)
                        Ub = 1/((1/hi)+(esp/Kpared))
                        S1=alpha1*H
                        S2= trans*alpha2*H
    #Calculo de conveccion vidrio-aire
                        Tm=(Tg+Tf)/2
                        B=round(1.00/Tm,4)
                        deltaT=Tg-Tf
                        uf=(1.846+0.00472*(Tm-300))*0.00001
                        pf=(1.1614-0.00353*(Tm-300))
                        kf=(0.0263+0.000074*(Tm-300))
                        cf=(1.007+0.00004*(Tm-300))*1000
                        Pr=uf*cf/kf
                        vf=uf/pf
                        Ls=Lw+z/2.0
                        Gr=(g*B*deltaT*(Ls**3))/vf**2
                        Ra=Gr*Pr
                        if (Ra < 10**9):
                            Nu=0.68+((0.67*(Ra**(1/4.0)))/((1+(0.492/Pr)**(9/16.0))**(4/9.0)))
                        else:
                            Nu=(0.825+((0.387*(Ra**(1/6.0)))/(1+((0.492/Pr)**(9/16.0)))**(8/27.0)))**2
                        h=Nu*kf/Ls
    #Calculo de conveccion aire-pared
                        Tm1=(Tw+Tf)/2
                        B1=1.0/Tm1
                        deltaT1=Tw-Tf
                        uf1=(1.846+0.00472*(Tm1-300))*0.00001
                        pf1=(1.1614-0.00353*(Tm1-300))
                        kf1=(0.0263+0.000074*(Tm1-300))
                        cf1=(1.007+0.00004*(Tm1-300))*1000
                        Pr1=uf1*cf1/kf1
                        vf1=uf1/pf1
                        Gr1=g*B1*deltaT1*Ls**3/vf1**2
                        Ra1=Gr1*Pr1
                        if (Ra1 < 10**9):
                            Nu1=0.68+((0.67*(Ra1**(1/4.0)))/((1+(0.492/Pr1)**(9/16.0))**(4/9.0)))
                        else:
                            Nu1=(0.825+((0.387*(Ra1**(1/6.0)))/(1+((0.492/Pr1)**(9/16.0)))**(8/27.0)))**2
                        h1=Nu1*kf1/Ls
                        m=(0.6)*((po*Ao)/((1+Ar)**(1/2.0)))*(((2*9.8*Lw*(Tf-Ta))/Ta)**(1/2.0))
                        resta1 = ((h*Tg)-((h+h1+(m*cf)/(0.75*W*Lw))*Tf)+(h1*Tw)) - (((m*cf)/(0.75*W*Lw))*Ta)
                        resta2 = ((-hrwg*Tg)-(h1*Tf)+((h1+hrwg+Ub)*Tw)) - (S2+(Ub*Ta))
                        resta = ((h+hrwg+Ut)*Tg-h*Tf-hrwg*Tw) - (S1+Ut*Ta)
                        if (resta < 0):
                            resta = resta * -1
                        if (resta1 < 0):
                            resta1 = resta1 * -1
                        if (resta2 < 0):
                            resta2 = resta2 * -1
                        valor = (resta2 + resta1 + resta) / 3.000
                        if (valor == 0):
                            contenedorCero.append([datoExcel, "Igualado a 0 ",Tg, Tf, Tw])
                        elif (valor < valorF):
                            valorF = valor
                            mejorTgP = Tg
                            mejorTfP = Tf
                            mejorTwP = Tw

                    Tf = Tf + 0.3
                Tw = Tw + 0.3
            Tg = Tg + 0.3
        #Ts=0.0552^Ta^1.5
#        hrs=(5.67*10^-8*Eg*(Tg+Ts)*(Tg^2+Ts^2)*(Tg-Ts))/(Tg-Ta)
        contenedor.append([datoExcel, mejorTgP, mejorTfP, mejorTwP, valorF, 'IteracionesRealizadas', a])
'''       print a
        print 'positivo'
        print mejorTgP
        print mejorTfP
        print mejorTwP

        print 'negativo'
        print mejorTgN
        print mejorTfN
        print mejorTwN
        print restaFN
        print datoExcel[1] '''
with open("/home/manuel/andreitaTest/juanpi/Output.csv", "w") as text_file:
    for content in contenedor:
        text_file.write(format(content))
        text_file.write(format("\n"))
    for content in contenedorCero:
        text_file.write(format(content))
        text_file.write(format(" igualado a 0\n"))


