      SUBROUTINE UHARD(SYIELD,HARD,EQPLAS,EQPLASRT,TIME,DTIME,TEMP,
     1     DTEMP,NOEL,NPT,LAYER,KSPT,KSTEP,KINC,CMNAME,NSTATV,
     2     STATEV,NUMFIELDV,PREDEF,DPRED,NUMPROPS,PROPS)
C
	  INCLUDE 'aba_param_dp.INC'
C
	  CHARACTER*80 CMNAME
	  DIMENSION HARD(3), STATEV(NSTATV), TIME(1), PREDEF(NUMFIELDV), DPRED(NUMFIELDV), PROPS(*)
	  REAL*8 C1,C3,C4,C5,C6,n,e,edot,edot0,edotn,T,Sp,einv,edinv
	  REAL*8 Eath,Eth,Eth_e,Eth_ed,Eth_T,EDexp
      C2 = PROPS(1)
      C3 = PROPS(2)
      C4 = PROPS(3)
      C6 = PROPS(4)
      edot0 = PROPS(5)

      e = max(EQPLAS, 1e-6)
      einv = 1.0 / max(e, 1.0D-2)
      edot = EQPLASRT
      edotn = max(edot / edot0, 1.0D-3)
      edinv = 1.0 / max(edotn, 1.0D-2)
      T = TEMP

      Eath = C6

      EDexp = -C3 + C4 * log(edotn)
      Eth = C2 * (e ** 0.5D0) * exp(T * EDexp)
      Eth_e = 0.5D0 * C2 * (einv ** 0.5D0) * exp(T * EDexp)
      Eth_ed = C4 * T * edinv * Eth
      Eth_T = EDexp * Eth

      SYIELD = Eth + Eath
      HARD(1) = Eth_e
      HARD(2) = Eth_ed
      HARD(3) = Eth_T

      return
      end