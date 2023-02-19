C--: Configurations for SPEEDY 41.5

C--  Model Parameters
C--:   NSTEPS = No. of time steps in one day
      NSTEPS = {nstep}
C--:   NSTDIA = Period (no. of steps) for diagnostic print-out
      NSTDIA = {nstadia}

C--:   NMONTS = Integration length in months
      NMONTS = {nmonts}
C--:   NDAYSL = No. of days in the last month of int. (max=30)
      NDAYSL = {ndays}

C--    ISTART = Start flag (0: from rest, 1: from restart file)
      ISTART = {restart}

C--:   NSTPPR = Period (no. of steps) for post-processing 
      NSTPPR = 6
C--:   NSTOUT = Period (no. of steps) for time-mean output
      NSTOUT = -1
C--:   IDOUT  = daily output flag (0=no, 1=basic (Z500,PREC,MSLP,TEMP0), 2=full)
      IDOUT  = 0
C--:   NMONRS = Period (no. of months) for restart file update
      NMONRS = -1

C--:   ISEASC = Seasonal cycle flag (0=no, 1=yes)
      ISEASC = 1
C--:   IYEAR0 = Year of initial date (4-digit, eg 1900)
      IYEAR0 = 1979
C--:   IMONT0 = Month of initial date (1 to 12)
      IMONT0 = 1

C--:   NSTRAD = Period (no. of steps) for shortwave radiation 
      NSTRAD = 3
C--:   NSTRDF = Duration of random diabatic forcing ( 0 : no forcing, > 0 : no. of initial steps, < 0 : whole integration)    
      NSTRDF = 0
C--:   INDRDF = Initialization index for random diabatic forcing
      INDRDF = 1

C--:   ICLAND = Uses land-surface temp. anomalies
      ICLAND = 1
C--:   ICSEA = uses a slab-ocean model
      ICSEA  = 0
C--:   ICICE
      ICICE  = 1
C--:   ISSTAN = prescribed SST anomaly flag (0=no, 1=yes)
      ISSTAN = 1

C--:   ISSTY0 = initial year of observed SST anomaly file
      ISSTY0 = 1870
C--:   ISST0  = record in SST anomaly file corr. to the initial month    
      ISST0  = (IYEAR0-ISSTY0)*12+IMONT0

C--   Logical flags (common LFLAG1)
C--:   LPPRES = Flag to post-process upper-air fields on pressure levels 
      LPPRES = .true.
C--:   LCO2 = Flag to include exponential CO2 absorbtivity increase
      LCO2 = .false.
      
      HOURS = 0
      BLOCKHOURS = 24./FLOAT(NSTEPS)
