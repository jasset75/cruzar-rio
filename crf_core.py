"""
Estado Inicial:
{H1,Oa1,Ob1,M1,Aa1,Ab1,P1,L1,I}
Estado Objetivo:
{H0,Oa0,Ob0,M0,Aa0,Ab0,P0,L0,D}
"""
"""
Descripción Reglas de Producción:
"""
RS_01 = '[01|P -> D];R1: Mover Policía a la Derecha'
RS_02= '[02|P -> I];R2: Mover Policía a la Izquierda'
RS_03= '[03|H -> D];R3: Mover Padre a la Derecha'
RS_04 = '[04|H -> I];R4: Mover Padre a la Izquierda'
RS_05 = '[05|M -> D];R5: Mover Madre a la Derecha'
RS_06 = '[06|M -> I];R6: Mover Madre a la Izquierda'
RS_07 = '[07|P,Ox -> D];R7: Mover Policia con Niño a la Derecha'
RS_08 = '[08|P,Ax -> D];R8: Mover Policia con Niña a la Derecha'
RS_09 = '[09|P,L -> D];R9: Mover Policia con Ladron a la Derecha'
RS_10 = '[10|P,H -> D];R10: Mover Policia con Padre a la Derecha'
RS_11 = '[11|P,M -> D];R11: Mover Policia con Madre a la Derecha'
RS_12 = '[12|H,Ox -> D];R12: Mover Padre con Niño a la Derecha'
RS_13 = '[13|M,Ax -> D];R13: Mover Madre con Niña a la Derecha'
RS_14 = '[14|P,Ox -> I];R14: Mover Policia con Niño a la Izquierda'
RS_15 = '[15|P,Ax -> I];R15: Mover Policia con Niña a la Izquierda'
RS_16 = '[16|P,L -> I];R16: Mover Policia con Ladron a la Izquierda'
RS_17 = '[17|P,H -> I];R17: Mover Policia con Padre a la Izquierda'
RS_18 = '[18|P,M -> I];R18: Mover Policia con Madre a la Izquierda'
RS_19 = '[19|H,Ox -> I];R19: Mover Padre con Niño a la Izquierda'
RS_20 = '[20|M,Ax -> I];R20: Mover Madre con Niña a la Izquierda'
RS_21 = '[21|H,M -> D];R21: Mover Padre con Madre a la Derecha'
RS_22 = '[22|H,M -> I];R22: Mover Padre con Madre a la Izquierda'
"""
Actores
"""
H = 'H'
Oa = 'Oa'
Ob = 'Ob'
M = 'M'
Aa = 'Aa'
Ab = 'Ab'
P = 'P'
L = 'L'
B = 'B'
I = 1
D = 0

"""
Estados Significativos
"""
#estado inicial
EI = {H:I,Oa:I,Ob:I,M:I,Aa:I,Ab:I,P:I,L:I,B:I}
#estado final u objetivo
EF = {H:D,Oa:D,Ob:D,M:D,Aa:D,Ab:D,P:D,L:D,B:D}
"""
Funciones de las reglas de producción
"""
#unitarias
def r_1(estado):
  """
  R1: Mover Policía a la Derecha [P -> D]
  """
  estado[P]=D; estado[B]=D
def r_2(estado):
  """
  R2: Mover Policía a la Izquierda [P -> I]
  """
  estado[P]=I; estado[B]=I
def r_3(estado):
  """
  R3: Mover Padre a la Derecha [H -> D]
  """
  estado[H]=D; estado[B]=D
def r_4(estado):
  """
  R4: Mover Padre a la Izquierda [H -> I]
  """
  estado[H]=I; estado[B]=I
def r_5(estado):
  """
  R5: Mover Madre a la Derecha [M -> D]
  """
  estado[M]=D; estado[B]=D
def r_6(estado):
  """
  R6: Mover Madre a la Izquierda [M -> I]
  """
  estado[M]=I; estado[B]=I
#binarias
def r_7(estado):
  """
  R7: Mover Policia con Niño a la Derecha [P,Ox -> D]
  """
  estado[P]=D
  if estado[Oa] == I:
    estado[Oa] = D
  else:
    estado[Ob] = D
  estado[B]=D
def r_8(estado):
  """
  R8: Mover Policia con Niña a la Derecha [P,Ax -> D]
  """
  estado[P]=D
  if estado[Aa] == I:
    estado[Aa] = D
  else:
    estado[Ab] = D
  estado[B]=D
def r_9(estado):
  """
  R9: Mover Policia con Ladron a la Derecha [P,L -> D]
  """
  estado[P]=D; estado[L]=D; estado[B]=D
def r_10(estado):
  """
  R10: Mover Policia con Padre a la Derecha [P,H -> D]
  """
  estado[P]=D; estado[H]=D; estado[B]=D
def r_11(estado):
  """
  R11: Mover Policia con Madre a la Derecha [P,M -> D]
  """
  estado[P]=D; estado[M]=D; estado[B]=D
def r_12(estado):
  """
  R12: Mover Padre con Niño a la Derecha [H,Ox -> D]
  """
  estado[H]=D
  if estado[Oa] == I:
    estado[Oa] = D
  else:
    estado[Ob] = D
  estado[B]=D
def r_13(estado):
  """
  R13: Mover Madre con Niña a la Derecha [M,Ax -> D]
  """
  estado[M]=D
  if estado[Aa] == I:
    estado[Aa] = D
  else:
    estado[Ab] = D
  estado[B]=D
def r_14(estado):
  """
  R14: Mover Policia con Niño a la Izquierda [P,Ox -> I]
  """
  estado[P]=I
  if estado[Oa] == D:
    estado[Oa] = I
  else:
    estado[Ob] = I
  estado[B]=I
def r_15(estado):
  """
  R15: Mover Policia con Niña a la Izquierda [P,Ax -> I]
  """
  estado[P]=I;
  if estado[Aa] == D:
    estado[Aa] = I
  else:
    estado[Ab] = I
  estado[B]=I
def r_16(estado):
  """
  R16: Mover Policia con Ladron a la Izquierda [P,L -> I]
  """
  estado[P]=I; estado[L]=I; estado[B]=I
def r_17(estado):
  """
  R17: Mover Policia con Padre a la Izquierda [P,H -> I]
  """
  estado[P]=I; estado[H]=I; estado[B]=I
def r_18(estado):
  """
  R18: Mover Policia con Madre a la Izquierda [P,M -> I]
  """
  estado[P]=I; estado[M]=I; estado[B]=I
def r_19(estado):
  """
  R19: Mover Padre con Niño a la Izquierda [H,Ox -> I]
  """
  estado[H]=I;
  if estado[Oa] == D:
    estado[Oa] = I
  else:
    estado[Ob] = I
  estado[B]=I
def r_20(estado):
  """
  R20: Mover Madre con Niña a la Izquierda [M,Ax -> I]
  """
  estado[M]=I;
  if estado[Aa] == D:
    estado[Aa] = I
  else:
    estado[Ab] = I
  estado[B]=I
def r_21(estado):
  """
  R21: Mover Padre con Madre a la Derecha [H,M -> D]
  """
  estado[H]=D; estado[M]=D; estado[B]=D
def r_22(estado):
  """
  R22: Mover Padre con Madre a la Izquierda [H,M -> I]
  """
  estado[H]=I; estado[M]=I; estado[B]=I
"""
Restricciones:

Estados que no se pueden dar:
{H1,Oax,Obx,Mx,Aax,Abx,P0,L1,x} (representa 64 estados diferentes*)
{Hx,Oa1,Obx,Mx,Aax,Abx,P0,L1,x} (representa 64 estados diferentes*)
{Hx,Oax,Ob1,Mx,Aax,Abx,P0,L1,x} (representa 64 estados diferentes*)
{Hx,Oax,Obx,M1,Aax,Abx,P0,L1,x} (representa 64 estados diferentes*)
{Hx,Oax,Obx,Mx,Aa1,Abx,P0,L1,x} (representa 64 estados diferentes*)
{Hx,Oax,Obx,Mx,Aax,Ab1,P0,L1,x} (representa 64 estados diferentes*)
{H1,Oax,Obx,M0,Aa1,Abx,Px,Lx,x} (representa 64 estados diferentes*)
{H1,Oax,Obx,M0,Aax,Ab1,Px,Lx,x} (representa 64 estados diferentes*)
{H0,Oa1,Obx,M1,Aax,Abx,Px,Lx,x} (representa 64 estados diferentes*)
{H0,Oax,Ob1,M1,Aax,Abx,Px,Lx,x} (representa 64 estados diferentes*)

Primitivas para las pre y post-condiciones
"""
def x_y_en(x,y,lado,estado):
  return estado[x] == lado and\
    estado[y] == lado
def x_y_z_en(x,y,z,lado,estado):
  return estado[x] == lado and\
    estado[y] == lado and\
    estado[z] == lado
def x_y_or_not_x_en(x,y,lado,estado):
  #tanto x como y estan en lado o x no está en aquel lado
  return x_y_en(x,y,lado,estado) or estado[x] != lado
def l_solo(estado):
  return (
    estado[P] != estado[L] and
    estado[H] != estado[L] and
    estado[M] != estado[L] and
    estado[Oa] != estado[L] and
    estado[Ob] != estado[L] and
    estado[Aa] != estado[L] and
    estado[Ab] != estado[L]
  )
def l_solo_or_en(lado,estado):
  #Ladron solo o en lado
  return l_solo(estado) or estado[L] == lado
def not_x_or_con_y_en(x,y,lado,estado):
  #no x en lado o está con y en lado
  return estado[x] != lado or estado[y] == lado
def not_nina_or_m_en(lado,estado):
  #no niña en lado, o Madre en lado
  return estado[M] == lado or (
    estado[Aa] != lado and estado[Ab] != lado
  )
def not_nino_or_h_en(lado,estado):
  #no niño en lado, o Padre en lado
  return estado[H] == lado or (
    estado[Oa] != lado and estado[Ob] != lado
  )
"""
Pre-condiciones y Post-condiciones (Restricciones)
"""
def pr_1(estado):
  """
  R1: Mover Policía a la Derecha [P -> D]
  PR1_1: Policía, Balsa en la Izquierda
  """
  return x_y_en(P,B,I,estado)
def ps_1(estado):
  """
  PS1_1: Ladrón en la Derecha o Ladrón solo
  """
  return l_solo_or_en(D,estado)
def pr_2(estado):
  """
  R2: Mover Policía a la Izquierda [P -> I]
  PR2_1: Policía, Balsa en la Derecha
  """
  return x_y_en(P,B,D,estado)
def ps_2(estado):
  """
  PS2_1: Ladrón en la Izquierda o Ladrón solo
  """
  return l_solo_or_en(I,estado)
def pr_3(estado):
  """
  R3: Mover Padre a la Derecha [H -> D]
  PR3_1: Padre, Balsa en la Izquierda
  """
  return x_y_en(H,B,I,estado)
def ps_3(estado):
  """
  PS3_1: Ninguna niña en la Derecha, o Madre en la derecha
  PS3_2: No está el ladrón o está con el policía en la derecha
  """
  return not_nina_or_m_en(D,estado) and\
    not_x_or_con_y_en(L,P,D,estado)
def pr_4(estado):
  """
  R4: Mover Padre a la Izquierda [H -> I]
  PR4_1: Padre, Balsa en la Derecha
  """
  return x_y_en(H,B,D,estado)
def ps_4(estado):
  """
  PS4_1: Ninguna niña en la Izquierda, o Madre en la izquierda
  PS4_2: No está el ladrón o está con el policía en la izquierda
  """
  return not_nina_or_m_en(I,estado) and\
    not_x_or_con_y_en(L,P,I,estado)
def pr_5(estado):
  """
  R5: Mover Madre a la Derecha [M -> D]
  PR5_1: Madre, Balsa en la Izquierda
  """
  return x_y_en(M,B,I,estado)
def ps_5(estado):
  """
  PS5_1: Ningun niño en la Derecha, o Padre en la derecha
  PS5_2: No está el ladrón o está con el policía en la derecha
  """
  return not_nino_or_h_en(D,estado) and\
    not_x_or_con_y_en(L,P,D,estado)
def pr_6(estado):
  """
  R6: Mover Madre a la Izquierda [M -> I]
  PR6_1: Madre, Balsa en la Derecha
  """
  return x_y_en(M,B,D,estado)
def ps_6(estado):
  """
  PS6_1: Ningun niño en la Izquierda, o Padre en la izquierda
  PS6_2: No está el ladrón o está con el policía en la izquierda
  """
  return not_nino_or_h_en(I,estado) and\
    not_x_or_con_y_en(L,P,I,estado)
def pr_7(estado):
  """
  R7: Mover Policia con Niño a la Derecha [P,Ox -> D]
  PR7_1: Policía, Uno de los niños, Balsa en la Izquierda
  """
  return x_y_z_en(P,Oa,B,I,estado) or x_y_z_en(P,Ob,B,I,estado)
def ps_7(estado):
  """
  PS7_1: No está la Madre a la derecha o está también el padre
  PS7_2: Ladrón en la derecha o está solo
  """
  return x_y_or_not_x_en(M,H,D,estado) and l_solo_or_en(D,estado)
def pr_8(estado):
  """ 
  R8: Mover Policia con Niña a la Derecha [P,Ax -> D]
  PR8_1: Policía, Una de las niñas, Balsa en la Izquierda
  """
  return x_y_z_en(P,Aa,B,I,estado) or x_y_z_en(P,Ab,B,I,estado)
def ps_8(estado):
  """
  PS8_1: No está el Padre a la derecha o está también la Madre
  PS8_2: Ladrón en la derecha o está solo
  """
  return x_y_or_not_x_en(H,M,D,estado) and l_solo_or_en(D,estado)
def pr_9(estado):  
  """
  R9: Mover Policia con Ladron a la Derecha [P,L -> D]
  PR9_1: Policía, Ladrón, Balsa en la Izquierda
  """
  return x_y_z_en(P,L,B,I,estado)
def ps_9(estado):
  """
  No hay restricción a mover Policía y Ladrón de un lado a otro en el mismo viaje
  """
  return True
def pr_10(estado):
  """
  R10: Mover Policia con Padre a la Derecha [P,H -> D]
  PR10_1: Policía, Padre, Balsa en la Izquierda
  """
  return x_y_z_en(P,H,B,I,estado)
def ps_10(estado):
  """
  PS10_1: No hay ninguna niña en la derecha o está también la Madre
  PS10_2: Ladrón en la derecha o está solo
  """
  return not_nina_or_m_en(D,estado) and l_solo_or_en(D,estado)
def pr_11(estado):
  """
  R11: Mover Policia con Madre a la Derecha [P,M -> D]
  PR11_1: Policía, Madre, Balsa en la Izquierda
  """
  return x_y_z_en(P,M,B,I,estado)
def ps_11(estado):
  """
  PS11_1: No hay ningun niño en la derecha o está también el Padre
  PS11_2: Ladrón en la derecha o está solo
  """
  return not_nino_or_h_en(D,estado) and l_solo_or_en(D,estado)
def pr_12(estado):
  """
  R12: Mover Padre con Niño a la Derecha [H,Ox -> D]
  PR12_1: Padre, Uno de los niños, Balsa en la Izquierda
  """
  return x_y_z_en(H,Oa,B,I,estado) or x_y_z_en(H,Ob,B,I,estado)
def ps_12(estado):
  """
  PS12_1: No hay ninguna niña en la derecha o está también la Madre
  PS12_2: No está el ladrón en la derecha o está con el policía
  """
  return not_nina_or_m_en(D,estado) and not_x_or_con_y_en(L,P,D,estado)
def pr_13(estado):
  """
  R13: Mover Madre con Niña a la Derecha [M,Ax -> D]
  PR13_1: Madre, Una de las niñas, Balsa en la Izquierda
  """
  return x_y_z_en(M,Aa,B,I,estado) or x_y_z_en(M,Ab,B,I,estado)
def ps_13(estado):
  """
  PS13_1: No hay ningún niño en la derecha o está también el Padre
  PS13_2: No está el ladrón en la derecha o está con el policía
  """
  return not_nino_or_h_en(D,estado) and not_x_or_con_y_en(L,P,D,estado)
def pr_14(estado):
  """
  R14: Mover Policia con Niño a la Izquierda [P,Ox -> I]
  PR14_1: Policía, Uno de los niños, Balsa en la Derecha
  """
  return x_y_z_en(P,Oa,B,D,estado) or x_y_z_en(P,Ob,B,D,estado)
def ps_14(estado):
  """
  PS14_1: No está la Madre en la izquierda o está también el Padre
  PS14_2: Ladrón en la izquierda o está solo
  """
  return not_x_or_con_y_en(M,H,I,estado) and l_solo_or_en(I,estado)
def pr_15(estado):
  """
  R15: Mover Policia con Niña a la Izquierda [P,Ax -> I]
  PR15_1: Policía, Una de las niñas, Balsa en la Derecha
  """
  return x_y_z_en(P,Aa,B,D,estado) or x_y_z_en(P,Ab,B,D,estado)
def ps_15(estado):
  """
  PS15_1: No está el Padre en la izquierda o está también la Madre
  PS15_2: Ladrón en la izquierda o está solo
  """
  return x_y_or_not_x_en(H,M,I,estado) and l_solo_or_en(I,estado)
def pr_16(estado):
  """
  R16: Mover Policia con Ladron a la Izquierda [P,L -> I]
  PR16_1: Policía, Ladrón, Balsa en la Derecha
  """
  return x_y_z_en(P,L,B,D,estado)
def ps_16(estado):
  """
  No hay restricción para mover ladrón y policía en el mismo viaje
  """
  return True
def pr_17(estado):
  """
  R17: Mover Policia con Padre a la Izquierda [P,H -> I]
  PR17_1: Policía, Padre, Balsa en la Derecha
  """
  return x_y_z_en(P,H,B,D,estado)
def ps_17(estado):
  """
  PS17_1: No hay ninguna niña en la izquierda o está también la Madre
  PS17_2: Ladrón en la izquierda o está solo
  """
  return not_nina_or_m_en(I,estado) and l_solo_or_en(I,estado)
def pr_18(estado):
  """
  R18: Mover Policia con Madre a la Izquierda [P,M -> I]
  PR18_1: Policía, Madre, Balsa en la Derecha
  """
  return x_y_z_en(P,M,B,D,estado)
def ps_18(estado):
  """
  PS18_1: No hay ningun niño en la izquierda o está también el Padre
  PS18_2: Ladrón en la izquierda o está solo
  """
  return not_nino_or_h_en(I,estado) and l_solo_or_en(I,estado)
def pr_19(estado):
  """
  R19: Mover Padre con Niño a la Izquierda [H,Ox -> I]
  PR19_1: Padre, Uno de los niños, Balsa en la Derecha
  """
  return x_y_z_en(H,Oa,B,D,estado) or x_y_z_en(H,Ob,B,D,estado)
def ps_19(estado):
  """
  PS19_1: No hay ninguna niña en la izquierda o está también la Madre
  PS19_2: No está el ladrón en la izquierda o está con el policía
  """
  return not_nina_or_m_en(I,estado) and not_x_or_con_y_en(L,P,I,estado)
def pr_20(estado):
  """
  R20: Mover Madre con Niña a la Izquierda [M,Ax -> I]
  PR20_1: Madre, Una de las niñas, Balsa en la Derecha
  """
  return x_y_z_en(M,Aa,B,D,estado) or x_y_z_en(M,Ab,B,D,estado)
def ps_20(estado):
  """
  PS20_1: No hay ningún niño en la izquierda o está también el Padre
  PS20_2: No está el ladrón en la izquierda o está con el policía
  """
  return not_nino_or_h_en(I,estado) and not_x_or_con_y_en(L,P,I,estado)
def pr_21(estado):
  """
  R21: Mover Padre con Madre a la Derecha [H,M -> D]
  PR21_1: Padre, Madre, Balsa en la Izquierda
  """
  return x_y_z_en(H,M,B,I,estado)
def ps_21(estado):
  """
  PS21_1: No está el ladrón en la derecha o está con el policía
  """
  return x_y_or_not_x_en(L,P,D,estado)
def pr_22(estado):
  """
  R22: Mover Padre con Madre a la Izquierda [H,M -> I]
  PR22_1: Padre, Madre, Balsa en la Derecha
  """
  return x_y_z_en(H,M,B,D,estado)
def ps_22(estado):
  """
  PS22_1: No está el ladrón en la izquierda o está con el policía
  """
  return x_y_or_not_x_en(L,P,I,estado)
"""
reglas
"""
RP = [None]*22
RP[0] = (pr_1,r_1,ps_1)
RP[1] = (pr_2,r_2,ps_2)
RP[2] = (pr_3,r_3,ps_3)
RP[3] = (pr_4,r_4,ps_4)
RP[4] = (pr_5,r_5,ps_5)
RP[5] = (pr_6,r_6,ps_6)
RP[6] = (pr_7,r_7,ps_7)
RP[7] = (pr_8,r_8,ps_8)
RP[8] = (pr_9,r_9,ps_9)
RP[9] = (pr_10,r_10,ps_10)
RP[10] = (pr_11,r_11,ps_11)
RP[11] = (pr_12,r_12,ps_12)
RP[12] = (pr_13,r_13,ps_13)
RP[13] = (pr_14,r_14,ps_14)
RP[14] = (pr_15,r_15,ps_15)
RP[15] = (pr_16,r_16,ps_16)
RP[16] = (pr_17,r_17,ps_17)
RP[17] = (pr_18,r_18,ps_18)
RP[18] = (pr_19,r_19,ps_19)
RP[19] = (pr_20,r_20,ps_20)
RP[20] = (pr_21,r_21,ps_21)
RP[21] = (pr_22,r_22,ps_22)
"""
Utilidades
"""
def regla_to_str(numero,short=True):
  regla = eval('RS_'+str(numero).zfill(2))
  if short:
    return regla.split(';')[0]
  else:
    s,l = regla.split(';')
    return '{0} :: {1}'.format(s,l)
def estado_to_str(estado):
  if estado[B]:
    lado = 'I'
  else:
    lado = 'D'
  str_estado ='{{H={},Oa={},Ob={},M={},Aa={},Ab={},P={},L={},B={}}}'.format(
    estado[H],
    estado[Oa],
    estado[Ob],
    estado[M],
    estado[Aa],
    estado[Ab],
    estado[P],
    estado[L],
    lado,
  )
  return str_estado
def reglas_posibles(reglas,estado,numero):
  rp = []
  for n in range(numero-1,len(reglas)):
    if reglas[n][0](estado):
      rp.append(n+1)
  return rp
def check_estado_final(estado):
  return estado[H]==EF[H] and\
    estado[Oa]==EF[Oa] and\
    estado[Ob]==EF[Ob] and\
    estado[M]==EF[M] and\
    estado[Aa]==EF[Aa] and\
    estado[Ab]==EF[Ab] and\
    estado[P]==EF[P] and\
    estado[L]==EF[L] and\
    estado[B]==EF[B]
def aplicar_regla(reglas,estado,numero):
  if numero < 1 or numero > len(reglas):
    raise Exception('Número de regla no válido (valores entre 1-22).')
  tupla = reglas[numero-1]
  #chequea precondicion
  if not tupla[0](estado):
    return Exception('La precondición para la regla R{0} no se cumple.'.format(numero))
  #aplica regla
  tupla[1](estado)
  #chequea postcondicion
  if tupla[2](estado):
    return True
  else:
    return False
