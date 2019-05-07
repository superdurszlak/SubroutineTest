      SUBROUTINE UHARD(SYIELD,HARD,EQPLAS,EQPLASRT,TIME,DTIME,TEMP,
     1     DTEMP,NOEL,NPT,LAYER,KSPT,KSTEP,KINC,CMNAME,NSTATV,
     2     STATEV,NUMFIELDV,PREDEF,DPRED,NUMPROPS,PROPS)
C
	  INCLUDE 'aba_param.INC'
C
	  CHARACTER*80 CMNAME
	  DIMENSION HARD(3), STATEV(NSTATV), TIME(1), PREDEF(NUMFIELDV), DPRED(NUMFIELDV), PROPS(*)
	  REAL*8 A,B,n0,n1,C,m,e,edot,T,Tr,Tm,Th,einv,edinv,edlog,D0,Dlog
	  REAL*8 Ehard, Ehard_e, Ehard_ed, EDhard, EDhard_ed, Tsoft, Tsoft_T
      A = PROPS(1)
      B = PROPS(2)
      n0 = PROPS(3)
      n1 = PROPS(4)
      C = PROPS(5)
      m = PROPS(6)
      Tr = PROPS(7)
      Tm = PROPS(8)

      D0 = 1.0D6
      Dlog = log(D0)
      e = max(EQPLAS, 1.0D-6)
      einv = 1.0D0 / max(e, 1.0D-2)
      edot = max(EQPLASRT, 1.0D-6)
      edlog = max(log(edot), 1.0D-2)
      edinv = 1.0D0 / max(edotn, 1.0D-2)
      T = TEMPOLD(km)
      Th = (T - Tr) / (Tm - Tr)
      Th = min(1.0D0, max(0.0D0, Th))

      Ehard = A + B * (e ** n0) * (1.0D0 - (edlog/Dlog) ** n1)
      Ehard_e = B * n0 * (einv ** (1.0D0 - n0)) * (1 - (edlog/Dlog) ** n1)
      Ehard_ed = - B * (e ** n0) * ((edinv / Dlog) ** n1) * n1 * ((Dlog/edlog) ** (1.0D0 - n1))

      EDhard = edot ** C
      EDhard_ed = C * edinv ** (1.0D0 - C)

      Tsoft = 1.0D0 - Th ** m
      Tsoft_T = m * (Th ** m) / min(Tr - T, -1.0D-3)

      SYIELD = Ehard * EDhard * Tsoft
      HARD(1) = Ehard_e * EDhard * Tsoft
      HARD(2) = Ehard * EDhard_ed * Tsoft + Ehard_ed * EDhard * Tsoft
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
      INCLUDE 'vaba_param.INC'
C
      DIMENSION PROPS(NPROPS), TEMPOLD(NBLOCK), TEMPNEW(NBLOCK),
     1   FIELDOLD(NBLOCK,NFIELDV), FIELDNEW(NBLOCK,NFIELDV),
     2   STATEOLD(NBLOCK,NSTATEV), EQPS(NBLOCK), EQPSRATE(NBLOCK),
     3   YIELD(NBLOCK), DYIELDDTEMP(NBLOCK), DYIELDDEQPS(NBLOCK,2),
     4   STATENEW(NBLOCK,NSTATEV), JELEM(NBLOCK)
C
      CHARACTER*80 CMNAME
C
	  REAL*8 A,B,n0,n1,C,m,e,edot,T,Tr,Tm,Th,einv,edinv,edlog,D0,Dlog
	  REAL*8 Ehard, Ehard_e, Ehard_ed, EDhard, EDhard_ed, Tsoft, Tsoft_T

      DO 100 km = 1,NBLOCK
          A = PROPS(1)
          B = PROPS(2)
          n0 = PROPS(3)
          n1 = PROPS(4)
          C = PROPS(5)
          m = PROPS(6)
          Tr = PROPS(7)
          Tm = PROPS(8)

          D0 = 1.0D6
          Dlog = log(D0)
          e = max(EQPS(km), 1.0D-6)
          einv = 1.0D0 / max(e, 1.0D-2)
          edot = max(EQPSRATE(km), 1.0D-6)
          edlog = max(log(edot), 1.0D-2)
          edinv = 1.0D0 / max(edotn, 1.0D-2)
          T = TEMP
          Th = (T - Tr) / (Tm - Tr)
          Th = min(1.0D0, max(0.0D0, Th))

          Ehard = A + B * (e ** n0) * (1.0D0 - (edlog/Dlog) ** n1)
          Ehard_e = B * n0 * (einv ** (1.0D0 - n0)) * (1 - (edlog/Dlog) ** n1)
          Ehard_ed = - B * (e ** n0) * ((edinv / Dlog) ** n1) * n1 * ((Dlog/edlog) ** (1.0D0 - n1))

          EDhard = edot ** C
          EDhard_ed = C * edinv ** (1.0D0 - C)

          Tsoft = 1.0D0 - Th ** m
          Tsoft_T = m * (Th ** m) / min(Tr - T, -1.0D-3)

          YIELD(km) = Ehard * EDhard * Tsoft
          DYIELDDEQPS(km,1) = Ehard_e * EDhard * Tsoft
          DYIELDDEQPS(km,2) = Ehard * EDhard_ed * Tsoft + Ehard_ed * EDhard * Tsoft
          DYIELDDTEMP(3) = Ehard * EDhard * Tsoft_T
  100 CONTINUE
C
      RETURN
      END