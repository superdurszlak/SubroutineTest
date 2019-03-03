      SUBROUTINE UHARD(SYIELD,HARD,EQPLAS,EQPLASRT,TIME,DTIME,TEMP,
     1     DTEMP,NOEL,NPT,LAYER,KSPT,KSTEP,KINC,CMNAME,NSTATV,
     2     STATEV,NUMFIELDV,PREDEF,DPRED,NUMPROPS,PROPS)
C
	  INCLUDE 'aba_param_dp.INC'
C
	  CHARACTER*80 CMNAME
	  DIMENSION HARD(3), STATEV(NSTATV), TIME(1), PREDEF(NUMFIELDV), DPRED(NUMFIELDV), PROPS(*)
	  REAL*8 A,B,n,C,m,e,edot,edot0,edotn,T,Tr,Tm,Th,Sp,Spmin
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

      Sp = (A + B*(e ** n)) *
     1  (1 + C*log(edotn)) *
     2  (1 - Th**m)
      HARD(1) = B*n*(e ** (n - 1)) *
     1  (1 + C*log(edotn)) *
     2  (1 - Th**m)
      HARD(2) = (A + B*(e ** n)) *
     1  (C/edot) *
     2  (1 - Th**m)
      HARD(3) = (A + B*(e ** n)) *
     1  (1 + C*log(edotn)) *
     2  (m * (Th ** m) / (Tr - T))

      Spmin = 1.0d0
      if (Sp.LE.Spmin) then
        Sp = Spmin
        HARD(1) = HARD(1)/1000
        HARD(2) = HARD(2)/1000
        HARD(3) = HARD(3)/1000
      end if
      SYIELD = Sp

      return
      end