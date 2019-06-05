      SUBROUTINE UHARD(SYIELD,HARD,EQPLAS,EQPLASRT,TIME,DTIME,TEMP,
     1     DTEMP,NOEL,NPT,LAYER,KSPT,KSTEP,KINC,CMNAME,NSTATV,
     2     STATEV,NUMFIELDV,PREDEF,DPRED,NUMPROPS,PROPS)
C
	  INCLUDE '../aba_param_dp.INC'
C
	  CHARACTER*80 CMNAME
	  DIMENSION HARD(3), STATEV(NSTATV), TIME(1), PREDEF(NUMFIELDV), DPRED(NUMFIELDV), PROPS(*)
	  REAL*8 C1,C3,C4,C5,C6,n,e,edot,edot0,edotn,T,Sp,einv,edinv
	  REAL*8 Eath,Eath_e,Eth,Eth_ed,Eth_T,EDexp
      C1 = PROPS(1)
      C3 = PROPS(2)
      C4 = PROPS(3)
      C5 = PROPS(4)
      n = PROPS(5)
      C6 = PROPS(6)
      edot0 = PROPS(7)

      e = max(EQPLAS, 1e-6)
      einv = 1.0 / max(e, 1.0D-2)
      edot = EQPLASRT
      edotn = max(edot / edot0, 1.0D-3)
      edinv = 1.0 / max(edotn, 1.0D-2)
      T = TEMP

      Eath = C5 * (e ** n) + C6
      Eath_e = C5 * n * (einv ** (1.0D0 - n))

      EDexp = -C3 + C4 * log(edotn)
      Eth = C1 * exp(T * EDexp)
      Eth_ed = C4 * T * edinv * Eth
      Eth_T = EDexp * Eth

      SYIELD = Eth + Eath
      HARD(1) = Eath_e
      HARD(2) = Eth_ed
      HARD(3) = Eth_T

      RETURN
      END


      SUBROUTINE VUHARD(
C READ ONLY -
     *     NBLOCK,
     *     JELEM, KINTPT, KLAYER, KSECPT,
     *     LANNEAL, STEPTIME, TOTALTIME, DT, CMNAME,
     *     NSTATEV, NFIELDV, NPROPS,
     *     PROPS, TEMPOLD, TEMPNEW, FIELDOLD, FIELDNEW,
     *     STATEOLD,
     *     EQPS, EQPSRATE,
C WRITE ONLY -
     *     YIELD, DYIELDDTEMP, DYIELDDEQPS,
     *     STATENEW )
C
      INCLUDE '../vaba_param_dp.INC'
C
      DIMENSION PROPS(NPROPS), TEMPOLD(NBLOCK), TEMPNEW(NBLOCK),
     1   FIELDOLD(NBLOCK,NFIELDV), FIELDNEW(NBLOCK,NFIELDV),
     2   STATEOLD(NBLOCK,NSTATEV), EQPS(NBLOCK), EQPSRATE(NBLOCK),
     3   YIELD(NBLOCK), DYIELDDTEMP(NBLOCK), DYIELDDEQPS(NBLOCK,2),
     4   STATENEW(NBLOCK,NSTATEV), JELEM(NBLOCK)
C
      CHARACTER*80 CMNAME
C
	  REAL*8 C1,C3,C4,C5,C6,n,e,edot,edot0,edotn,T,Sp,einv,edinv
	  REAL*8 Eath,Eath_e,Eth,Eth_ed,Eth_T,EDexp

      DO 100 km = 1,NBLOCK
          C1 = PROPS(1)
          C3 = PROPS(2)
          C4 = PROPS(3)
          C5 = PROPS(4)
          n = PROPS(5)
          C6 = PROPS(6)
          edot0 = PROPS(7)

          e = max(EQPS(km), 1e-6)
          einv = 1.0 / max(e, 1.0D-2)
          edot = EQPSRATE(km)
          edotn = max(edot / edot0, 1.0D-3)
          edinv = 1.0 / max(edotn, 1.0D-2)
          T = TEMPOLD(km)

          Eath = C5 * (e ** n) + C6
          Eath_e = C5 * n * (einv ** (1.0D0 - n))

          EDexp = -C3 + C4 * log(edotn)
          Eth = C1 * exp(T * EDexp)
          Eth_ed = C4 * T * edinv * Eth
          Eth_T = EDexp * Eth

          YIELD(km) = Eth + Eath
          DYIELDDEQPS(km,1) = Eath_e
          DYIELDDEQPS(km,2) = Eth_ed
          DYIELDDTEMP(km) = Eth_T
  100 CONTINUE
C
      RETURN
      END