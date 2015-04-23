'''
Created on 23/4/2015

@author: Mathieu De Valery 10-10193
@author: Oscar Guillen 
'''

import unittest
from calcularPrecio import *
from datetime import *
from decimal import Decimal


class PruebaReserva(unittest.TestCase):
    
    def testtarifaNegativa(self):
        #Caso de prueba para tarifas negativas
        pruebaTarifa = Tarifa(-1,-2)
        reservaInicial = datetime(2015,1,2,10,40,0,0)
        reservaFinal = datetime(2015,1,2,11,0,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        self.assertRaises(Exception,calcularPrecio, pruebaTarifa, tiempoDeReserva)
        
    def testtarifaMenor15min(self):
        #Caso de prueba para tarifas menor de 15 min
        pruebaTarifa = Tarifa(3,5)
        reservaInicial = datetime(2015,1,2,10,40,0,0)
        reservaFinal = datetime(2015,1,2,10,45,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        self.assertRaises(Exception,calcularPrecio, pruebaTarifa, tiempoDeReserva) 
        
    def testtarifaFechainiMenorFechafin(self):
        #Caso de prueba para tarifas con fecha incial mayor a la fecha final.
        pruebaTarifa = Tarifa(3,5)
        reservaInicial = datetime(2015,1,2,10,40,0,0)
        reservaFinal = datetime(2015,1,2,10,20,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        self.assertRaises(Exception,calcularPrecio, pruebaTarifa, tiempoDeReserva)        
        
    
        
    def testtarifa15min(self):
        #Caso de prueba para tarifas con tiempo 15 minutos
        pruebaTarifa = Tarifa(1,5)
        reservaInicial = datetime(2015,1,2,10,40,0,0)
        reservaFinal = datetime(2015,1,2,10,55,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        precio = calcularPrecio(pruebaTarifa,tiempoDeReserva)
        self.assertEqual(precio, Decimal((1*15)/60))
        
    def testReservacionMax7d(self):
        #Caso de prueba para verificar que la reservacion no sea mayor a 7 dias
        pruebaTarifa = Tarifa(3,5)
        reservaInicial = datetime(2015,1,2,10,40,0,0)
        reservaFinal = datetime(2015,1,9,10,40,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        precio = calcularPrecio(pruebaTarifa,tiempoDeReserva)
        self.assertEqual(precio,((3*7200)/60)+((2880*5)/60))
    
    def testReservacionExcedio7d(self):
        #Caso de prueba para verificar que la reservacion es mayor a 7 dias.
        pruebaTarifa = Tarifa(3,5)
        reservaInicial = datetime(2015,1,2,10,40,0,0)
        reservaFinal = datetime(2015,1,9,10,41,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        self.assertRaises(Exception, calcularPrecio, pruebaTarifa, tiempoDeReserva)  
        
    def testReservacionSemana(self):
        #Caso de prueba para verificar una reservacion entre semana
        pruebaTarifa = Tarifa(3,5)
        reservaInicial = datetime(2015,4,22,10,40,0,0)
        reservaFinal = datetime(2015,4,24,10,40,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        precio = calcularPrecio(pruebaTarifa,tiempoDeReserva)
        self.assertEqual(precio, (3*2880)/60)
        
    def testReservacionFinSemana(self):
        #Caso de prueba para verificar una reservacion en fin de semana
        pruebaTarifa = Tarifa(3,5)
        reservaInicial = datetime(2015,4,25,10,40,0,0)
        reservaFinal = datetime(2015,4,26,10,40,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        precio = calcularPrecio(pruebaTarifa,tiempoDeReserva)
        self.assertEqual(precio, (5*1440)/60)
        
    def testReservacionFinSemanaySemana(self):
        #Caso de prueba para verificar una reservacion que va de una
        #semana a otra pasando por un fin de semana.
        pruebaTarifa = Tarifa(3,5)
        reservaInicial = datetime(2015,4,23,10,40,0,0)
        reservaFinal = datetime(2015,4,28,10,40,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        precio = calcularPrecio(pruebaTarifa,tiempoDeReserva)
        self.assertEqual(precio, round(Decimal(((2880*5)/60) + ((4320*3)/60)),2))

    def testReservacionUnDia(self):
        #Caso de prueba para verificar una reservacion de un dia completo.
        pruebaTarifa = Tarifa(3,5)
        reservaInicial = datetime(2015,4,25,0,0,0,0)
        reservaFinal = datetime(2015,4,25,23,59,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        precio = calcularPrecio(pruebaTarifa,tiempoDeReserva)
        self.assertEqual(precio, round(Decimal((5*1439)/60),2))       
        
    def testReservacionTarifaAlta(self):
        #Caso de prueba para verificar una reservacion con una tarifa alta.
        # en este caso con la tarifa de fin de semana.
        pruebaTarifa = Tarifa(2**31-1,2**32-1)
        reservaInicial = datetime(2015,4,25,10,40,0,0)
        reservaFinal = datetime(2015,4,28,10,40,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        precio = calcularPrecio(pruebaTarifa,tiempoDeReserva)
        self.assertEqual(precio, round(Decimal(((((2**31)-1)*2080)/60)+((((2**32)-1)*2240)/60)),2))
        
        
        
    def testReservacionTarifaBaja(self):
        #Caso de prueba para verificar una reservacion con tarifa muy baja.
        #EN este caso con tarifa de fin de semana.
        pruebaTarifa = Tarifa(0.00000003,0.00000005)
        reservaInicial = datetime(2015,4,25,10,40,0,0)
        reservaFinal = datetime(2015,4,28,10,40,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        precio = calcularPrecio(pruebaTarifa,tiempoDeReserva)
        self.assertEqual(precio, round(Decimal((((0.00000005)*2239)/60)+(((0.00000003)*2079)/60)),2))   
        
            
        
        
        



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
