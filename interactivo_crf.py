import sys
from crf_core import *

def is_int(s_int):
  try:
    int(s_int); return True
  except:
    return False
def pinta_movimiento_siguiente(r_posibles,estado):
  print('Estado Actual:')
  print('\t',estado_to_str(estado))
  print('Reglas de Producción factibles:')
  for r in r_posibles:
    print('\t',regla_to_str(r))
def imprime_info(estado):
  print('Estado Inicial:')
  print('\t',estado_to_str(EI))
  print('Estado Objetivo:')
  print('\t',estado_to_str(EF))
  print('Estado Actual:')
  print('\t',estado_to_str(estado))
  print('Reglas de Producción:')
  for n in range(1,len(RP)+1):
    print('\t',regla_to_str(n,short=False))
def jugada_to_str(jugada):
  return '=>'.join(map(regla_to_str,jugada))
def main():
  #para grabar la jugada completa
  jugada = []
  #partimos del estado inicial
  estado = EI
  #presentamos info por pantalla
  imprime_info(estado)
  #obtenemos la lista de reglas de producción posibles desde el estado actual
  l_rp = reglas_posibles(RP,estado,1)
  #sacamos información por pantalla de las posibles reglas
  pinta_movimiento_siguiente(l_rp,estado)
  #bucle del juego interactivo
  while True:
    sr = input('Introduce número de la siguiente regla, h (help), q (quit): ')
    if sr=='q':
      sys.exit(0)
    elif sr=='h':
      imprime_info(estado)
    else:
      if not is_int(sr) or not int(sr) in l_rp:
        print('"{0}" no es una regla posible!'.format(sr))
      else:
        i_sr = int(sr)
        jugada.append(i_sr)
        print('Escogiste {0}'.format(regla_to_str(i_sr)))
        #la regla no cumple la postcondición LOSE
        if not aplicar_regla(RP,estado,i_sr):
          print(estado_to_str(estado))
          print('Tú pierdes!')
          print(jugada_to_str(jugada))
          sys.exit(0)
        #la regla lleva al estdo final WIN
        elif check_estado_final(estado):
          print('Tú ganas!')
          print(jugada_to_str(jugada))
          sys.exit(0)
        #la regla lleva a un estado intermedio válido
        else:
          l_rp = reglas_posibles(RP,estado,1)
          pinta_movimiento_siguiente(l_rp,estado)

if __name__ == "__main__":
  main()