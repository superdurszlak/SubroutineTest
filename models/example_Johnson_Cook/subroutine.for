      SUBROUTINE UHARD(SYIELD,HARD,EQPLAS,EQPLASRT,TIME,DTIME,TEMP,
     1  DTEMP,NOEL,NPT,LAYER,KSPT,KSTEP,KINC,CMNAME,NSTATV,
     2  STATEV,NUMFIELDV,PREDEF,DPRED,NPROPS,PROPS)
C
	  INCLUDE 'aba_param_sp.INC'
C
	  CHARACTER*80 CMNAME
	  DIMENSION HARD(3), STATEV(NSTATV), TIME(1), PREDEF(NUMFIELDV), PROPS(NPROPS)
	  REAL*8 A,B,n,C,m,e,edot,edot0,edotn,T,Tr,Tm,Th
      A = PROPS(1)
      B = PROPS(2)
      C = PROPS(3)
      n = PROPS(4)
      m = PROPS(5)
      edot0 = PROPS(6)
      Tr = PROPS(7)
      Tm = PROPS(8)
      e = EQPLAS
      edot = EQPLASRT
      edotn = edot/edot0
      T = TEMP
      Th = (T - Tr)/(Tm - Tr)

      SYIELD = (A + B*(e ** n)) *
     1  (1 + C*log(edotn)) *
     2  ((1 - Th)**m)
      HARD(1) = B*n*(e ** (n - 1)) *
     1  (1 + C*log(edotn)) *
     2  ((1 - Th)**m)
      HARD(2) = (A + B*(e ** n)) *
     1  (C/edot) *
     2  ((1 - Th)**m)
      HARD(3) = (A + B*(e ** n)) *
     1  (1 + C*log(edotn)) *
     2  (T * m * ((Tm - Tr)/(Tm - Tr)) ** (m - 1))

      STATEV(1) = edot
      STATEV(2) = SYIELD
      STATEV(3) = HARD(1)
      STATEV(4) = HARD(2)
      STATEV(5) = HARD(3)
      return
      end