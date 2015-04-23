'''
Created on 23/4/2015

@author: Mathieu De Valery 10-10193
@author: Oscar Guillen 
'''

import unittest
from calcularPrecio import *
from datetime import *


class PruebaReserva(unittest.TestCase):
    
    def testtarifaNegativa(self):
        #Caso de prueba para tarifas negativas23
        pruebaTarifa = Tarifa(-1,-2)
        reservaInicial = datetime(2015,1,2,10,40,0,0)
        reservaFinal = datetime(2015,1,2,11,0,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        self.assertRaises(Exception,calcularPrecio, pruebaTarifa, tiempoDeReserva)
        
    def testtarifa15min(self):
        #Caso de prueba para tarifas con tiempo 15 minutos
        pruebaTarifa = Tarifa(1,5)
        reservaInicial = datetime(2015,1,2,10,40,0,0)
        reservaFinal = datetime(2015,1,2,10,55,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        precio = calcularPrecio(pruebaTarifa,tiempoDeReserva)
        self.assertEqual(precio, (1*15)/60)
        
    def testReservacionMax7d(self):
        #Caso de prueba para verificar que la reservacion no sea mayor a 7 dias
        pruebaTarifa = Tarifa(3,5)
        reservaInicial = datetime(2015,1,2,10,40,0,0)
        reservaFinal = datetime(2015,1,9,10,40,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        precio = calcularPrecio(pruebaTarifa,tiempoDeReserva)
        self.assertEqual(precio,((3*7200)/60)+((2880*5)/60))
    
    def testReservacionExcedio7d(self):
        #Caso de prueba para verificar que la reservacion es mayor a 7 dias
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
        
            
        
        
        



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()