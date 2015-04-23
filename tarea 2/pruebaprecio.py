'''
Created on 22/4/2015

@author: Mathieu De Valery 10-10193
@author: Oscar Guillen 
'''

import unittest
from calcularPrecio import *
from datetime import *

class PruebaReserva(unittest.TestCase):
    
    def tarifaNegativa(self):
        #Caso de prueba para tarifas negativas
        pruebaTarifa = Tarifa (-1,-2)
        reservaInicial = datetime(2015,1,2,10,40,0,0)
        reservaFinal = datetime(2015,1,2,11,0,0,0)
        tiempoDeReserva = [reservaInicial,reservaFinal]
        self.assertRaises(Exception,calcularPrecio, pruebaTarifa)
        
        
if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()        
        
