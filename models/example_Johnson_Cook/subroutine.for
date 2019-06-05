      SUBROUTINE UHARD(SYIELD,HARD,EQPLAS,EQPLASRT,TIME,DTIME,TEMP,
     1     DTEMP,NOEL,NPT,LAYER,KSPT,KSTEP,KINC,CMNAME,NSTATV,
     2     STATEV,NUMFIELDV,PREDEF,DPRED,NUMPROPS,PROPS)
C
	  INCLUDE '../aba_param_dp.INC'
C
	  CHARACTER*80 CMNAME
	  DIMENSION HARD(3), STATEV(NSTATV), TIME(1), PREDEF(NUMFIELDV), DPRED(NUMFIELDV), PROPS(*)
	  REAL*8 A,B,n,C,m,e,edot,edot0,edotn,T,Tr,Tm,Th,einv,edinv
	  REAL*8 Ehard, Ehard_e, EDhard, EDhard_ed, Tsoft, Tsoft_T
      A = PROPS(1)
      B = PROPS(2)
      C = PROPS(3)
      n = PROPS(4)
      m = PROPS(5)
      edot0 = PROPS(6)
      Tr = PROPS(7)
      Tm = PROPS(8)

      e = max(EQPLAS, 1e-6)
      einv = 1.0 / max(e, 1.0D-2)
      edot = EQPLASRT
      edotn = max(edot / edot0, 1.0D-3)
      edinv = 1.0 / max(edotn, 1.0D-2)
      T = TEMP
      Th = (T - Tr) / (Tm - Tr)

      Ehard = A + B * (e ** n)
      Ehard_e = B * n * (einv ** (1.0D0 - n))

      EDhard = 1 + C * log(edotn)
      EDhard_ed = C * edinv

      Tsoft = 1 - Th ** m
      Tsoft_T = m * (Th ** m) / (Tr - T)

      SYIELD = Ehard * EDhard * Tsoft
      HARD(1) = Ehard_e * EDhard * Tsoft
      HARD(2) = Ehard * EDhard_ed * Tsoft
      HARD(3) = Ehard * EDhard * Tsoft_T

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

	  REAL*8 A,B,n,C,m,e,edot,edot0,edotn,T,Tr,Tm,Th,einv,edinv
	  REAL*8 Ehard, Ehard_e, EDhard, EDhard_ed, Tsoft, Tsoft_T
C
      DO 100 km = 1,NBLOCK
          A = PROPS(1)
          B = PROPS(2)
          C = PROPS(3)
          n = PROPS(4)
          m = PROPS(5)
          edot0 = PROPS(6)
          Tr = PROPS(7)
          Tm = PROPS(8)

          e = max(EQPS(km), 1e-6)
          einv = 1.0 / max(e, 1.0D-2)
          edot = EQPSRATE(km)
          edotn = max(edot / edot0, 1.0D-3)
          edinv = 1.0 / max(edotn, 1.0D-2)
          T = TEMPOLD(km)
          Th = (T - Tr) / (Tm - Tr)

          Ehard = A + B * (e ** n)
          Ehard_e = B * n * (einv ** (1.0D0 - n))

          EDhard = 1 + C * log(edotn)
          EDhard_ed = C * edinv

          Tsoft = 1 - Th ** m
          Tsoft_T = m * (Th ** m) / (Tr - T)

          YIELD(km) = Ehard * EDhard * Tsoft
          DYIELDDEQPS(km,1) = Ehard_e * EDhard * Tsoft
          DYIELDDEQPS(km,2) = Ehard * EDhard_ed * Tsoft
          DYIELDDTEMP(km) = Ehard * EDhard * Tsoft_T
  100 CONTINUE
C
      RETURN
      END