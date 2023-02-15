C--:  NMONTS = Integration length in months
      NMONTS = 12
      NDAYSL = 0
      NSTEPS = 36
      NSTDIA = 36*5
      NSTPPR = 6
      NSTOUT = -1
      IDOUT  = 0
      NMONRS = -1
      ISEASC = 1
      IYEAR0 = 1979
      IMONT0 = 1
      NSTRAD = 3
      NSTRDF = 0
      INDRDF = 1
      ICLAND = 1
      ICSEA  = 0
      ICICE  = 1
      ISSTAN = 1
      ISSTY0 = 1870
      ISST0  = (IYEAR0-ISSTY0)*12+IMONT0
      LPPRES = .true.
      LCO2 = .false.
      

      NSTDIA = 96*5
      NSTPPR = 6

      istart = 0
      HOURS = 0
      BLOCKHOURS = 24./FLOAT(NSTEPS)
