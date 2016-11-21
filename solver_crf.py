import sys
from crf_core import *
"""
Clase para resolver el juego con IA
"""
class CruzarRioEnFamilia(object):
  _estado = EI
  _reglas = [None]*22
  _estado_ant = None
  _ultima_regla = None
  _siguiente_regla = 1
  def __init__(self):
    self._reglas = RP
  def __str__(self):
    if self._ultima_regla:
      str_estado = regla_to_str(self._ultima_regla)+':'+estado_to_str(self._estado)
    else:  
      str_estado = estado_to_str(self._estado)
    return str_estado
  def selec_regla(self,numero):
    for n in range(numero-1,len(self._reglas)):
      if self._reglas[n][0](self._estado):
        return n+1
  def aplicar_regla(self,numero,backtrack=True):
    if numero < 1 or numero > len(self._reglas):
      raise Exception('Número de regla no válido (valores entre 1-22).')
    tupla = self._reglas[numero-1]
    #chequea precondicion
    if not tupla[0](self._estado):
      return Exception('La precondición para la regla R{0} no se cumple.'.format(numero))
    self._estado_ant = self._estado
    #chequea postcondicion
    if tupla[1](self._estado):
      return True
    else:
      if backtrack:
        self._estado = self._estado_ant
      return False
  def aplicar_regla_auto(self,backtrack=True):
    #las reglas siempre empiezan en 1
    #el numero se corrige sumandole 1 tras aplicarle módulo con el tamaño de la lista
    import pdb; pdb.set_trace()
    if self.aplicar_regla(self._siguiente_regla,backtrack):
      self._ultima_regla = self._siguiente_regla
    self._siguiente_regla = 1+(self._siguiente_regla+1)%len(self._reglas)