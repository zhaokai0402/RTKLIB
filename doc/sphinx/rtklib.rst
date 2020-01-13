
.. _rtklib:

#########################
RTKLib 基础定义
#########################

.. contents:: 目录

.. _obsd_t:

obsd_t
========================

.. code-block::

    typedef struct {        /* observation data record */
        gtime_t time;       /* receiver sampling time (GPST) */
        unsigned char sat,rcv; /* satellite/receiver number */
        unsigned char SNR [NFREQ+NEXOBS]; /* signal strength (0.25 dBHz) */
        unsigned char LLI [NFREQ+NEXOBS]; /* loss of lock indicator */
        unsigned char code[NFREQ+NEXOBS]; /* code indicator (CODE_???) */
        double L[NFREQ+NEXOBS]; /* observation data carrier-phase (cycle) */
        double P[NFREQ+NEXOBS]; /* observation data pseudorange (m) */
        float  D[NFREQ+NEXOBS]; /* observation data doppler frequency (Hz) */
    } obsd_t;

.. _nav_t:

nav_t
========================

.. code-block::

    typedef struct {        /* navigation data type */
        int n,nmax;         /* number of broadcast ephemeris */
        int ng,ngmax;       /* number of glonass ephemeris */
        int ns,nsmax;       /* number of sbas ephemeris */
        int ne,nemax;       /* number of precise ephemeris */
        int nc,ncmax;       /* number of precise clock */
        int na,namax;       /* number of almanac data */
        int nt,ntmax;       /* number of tec grid data */
        int nn,nnmax;       /* number of stec grid data */
        eph_t *eph;         /* GPS/QZS/GAL ephemeris */
        geph_t *geph;       /* GLONASS ephemeris */
        seph_t *seph;       /* SBAS ephemeris */
        peph_t *peph;       /* precise ephemeris */
        pclk_t *pclk;       /* precise clock */
        alm_t *alm;         /* almanac data */
        tec_t *tec;         /* tec grid data */
        stec_t *stec;       /* stec grid data */
        erp_t  erp;         /* earth rotation parameters */
        double utc_gps[4];  /* GPS delta-UTC parameters {A0,A1,T,W} */
        double utc_glo[4];  /* GLONASS UTC GPS time parameters */
        double utc_gal[4];  /* Galileo UTC GPS time parameters */
        double utc_qzs[4];  /* QZS UTC GPS time parameters */
        double utc_cmp[4];  /* BeiDou UTC parameters */
        double utc_sbs[4];  /* SBAS UTC parameters */
        double ion_gps[8];  /* GPS iono model parameters {a0,a1,a2,a3,b0,b1,b2,b3} */
        double ion_gal[4];  /* Galileo iono model parameters {ai0,ai1,ai2,0} */
        double ion_qzs[8];  /* QZSS iono model parameters {a0,a1,a2,a3,b0,b1,b2,b3} */
        double ion_cmp[8];  /* BeiDou iono model parameters {a0,a1,a2,a3,b0,b1,b2,b3} */
        int leaps;          /* leap seconds (s) */
        double lam[MAXSAT][NFREQ]; /* carrier wave lengths (m) */
        double cbias[MAXSAT][3];   /* code bias (0:p1-p2,1:p1-c1,2:p2-c2) (m) */
        double wlbias[MAXSAT];     /* wide-lane bias (cycle) */
        double glo_cpbias[4];    /* glonass code-phase bias {1C,1P,2C,2P} (m) */
        char glo_fcn[MAXPRNGLO+1]; /* glonass frequency channel number + 8 */
        pcv_t pcvs[MAXSAT]; /* satellite antenna pcv */
        sbssat_t sbssat;    /* SBAS satellite corrections */
        sbsion_t sbsion[MAXBAND+1]; /* SBAS ionosphere corrections */
        dgps_t dgps[MAXSAT]; /* DGPS corrections */
        ssr_t ssr[MAXSAT];  /* SSR corrections */
        lexeph_t lexeph[MAXSAT]; /* LEX ephemeris */
        lexion_t lexion;    /* LEX ionosphere correction */
    } nav_t;

.. _prcopt_t:

prcopt_t
========================

.. code-block::

    typedef struct {        /* processing options type */
        int mode;           /* positioning mode (PMODE_???) */
        int soltype;        /* solution type (0:forward,1:backward,2:combined) */
        int nf;             /* number of frequencies (1:L1,2:L1+L2,3:L1+L2+L5) */
        int navsys;         /* navigation system */
        double elmin;       /* elevation mask angle (rad) */
        snrmask_t snrmask;  /* SNR mask */
        int sateph;         /* satellite ephemeris/clock (EPHOPT_???) */
        int modear;         /* AR mode (0:off,1:continuous,2:instantaneous,3:fix and hold,4:ppp-ar) */
        int glomodear;      /* GLONASS AR mode (0:off,1:on,2:auto cal,3:ext cal) */
        int bdsmodear;      /* BeiDou AR mode (0:off,1:on) */
        int maxout;         /* obs outage count to reset bias */
        int minlock;        /* min lock count to fix ambiguity */
        int minfix;         /* min fix count to hold ambiguity */
        int ionoopt;        /* ionosphere option (IONOOPT_???) */
        int tropopt;        /* troposphere option (TROPOPT_???) */
        int dynamics;       /* dynamics model (0:none,1:velociy,2:accel) */
        int tidecorr;       /* earth tide correction (0:off,1:solid,2:solid+otl+pole) */
        int niter;          /* number of filter iteration */
        int codesmooth;     /* code smoothing window size (0:none) */
        int intpref;        /* interpolate reference obs (for post mission) */
        int sbascorr;       /* SBAS correction options */
        int sbassatsel;     /* SBAS satellite selection (0:all) */
        int rovpos;         /* rover position for fixed mode */
        int refpos;         /* base position for relative mode */
                            /* (0:pos in prcopt,  1:average of single pos, */
                            /*  2:read from file, 3:rinex header, 4:rtcm pos) */
        double eratio[NFREQ]; /* code/phase error ratio */
        double err[5];      /* measurement error factor */
                            /* [0]:reserved */
                            /* [1-3]:error factor a/b/c of phase (m) */
                            /* [4]:doppler frequency (hz) */
        double std[3];      /* initial-state std [0]bias,[1]iono [2]trop */
        double prn[5];      /* process-noise std [0]bias,[1]iono [2]trop [3]acch [4]accv */
        double sclkstab;    /* satellite clock stability (sec/sec) */
        double thresar[4];  /* AR validation threshold */
        double elmaskar;    /* elevation mask of AR for rising satellite (deg) */
        double elmaskhold;  /* elevation mask to hold ambiguity (deg) */
        double thresslip;   /* slip threshold of geometry-free phase (m) */
        double maxtdiff;    /* max difference of time (sec) */
        double maxinno;     /* reject threshold of innovation (m) */
        double maxgdop;     /* reject threshold of gdop */
        double baseline[2]; /* baseline length constraint {const,sigma} (m) */
        double ru[3];       /* rover position for fixed mode {x,y,z} (ecef) (m) */
        double rb[3];       /* base position for relative mode {x,y,z} (ecef) (m) */
        char anttype[2][MAXANT]; /* antenna types {rover,base} */
        double antdel[2][3]; /* antenna delta {{rov_e,rov_n,rov_u},{ref_e,ref_n,ref_u}} */
        pcv_t pcvr[2];      /* receiver antenna parameters {rov,base} */
        unsigned char exsats[MAXSAT]; /* excluded satellites (1:excluded,2:included) */
        char rnxopt[2][256]; /* rinex options {rover,base} */
        int  posopt[6];     /* positioning options */
        int  syncsol;       /* solution sync mode (0:off,1:on) */
        double odisp[2][6*11]; /* ocean tide loading parameters {rov,base} */
        exterr_t exterr;    /* extended receiver error model */
    } prcopt_t;

.. _ssat_t:

ssat_t
========================

.. code-block::

    typedef struct {        /* satellite status type */
        unsigned char sys;  /* navigation system */
        unsigned char vs;   /* valid satellite flag single */
        double azel[2];     /* azimuth/elevation angles {az,el} (rad) */
        double resp[NFREQ]; /* residuals of pseudorange (m) */
        double resc[NFREQ]; /* residuals of carrier-phase (m) */
        unsigned char vsat[NFREQ]; /* valid satellite flag */
        unsigned char snr [NFREQ]; /* signal strength (0.25 dBHz) */
        unsigned char fix [NFREQ]; /* ambiguity fix flag (1:fix,2:float,3:hold) */
        unsigned char slip[NFREQ]; /* cycle-slip flag */
        unsigned int lock [NFREQ]; /* lock counter of phase */
        unsigned int outc [NFREQ]; /* obs outage counter of phase */
        unsigned int slipc[NFREQ]; /* cycle-slip counter */
        unsigned int rejc [NFREQ]; /* reject counter */
        double  gf;         /* geometry-free phase L1-L2 (m) */
        double  gf2;        /* geometry-free phase L1-L5 (m) */
        double  phw;        /* phase windup (cycle) */
        gtime_t pt[2][NFREQ]; /* previous carrier-phase time */
        double  ph[2][NFREQ]; /* previous carrier-phase observable (cycle) */
    } ssat_t;


.. _sol_t:

sol_t
========================

.. code-block::

    typedef struct {        /* solution type */
        gtime_t time;       /* time (GPST) */
        double rr[6];       /* position/velocity (m|m/s) */
                            /* {x,y,z,vx,vy,vz} or {e,n,u,ve,vn,vu} */
        float  qr[6];       /* position variance/covariance (m^2) */
                            /* {c_xx,c_yy,c_zz,c_xy,c_yz,c_zx} or */
                            /* {c_ee,c_nn,c_uu,c_en,c_nu,c_ue} */
        double dtr[6];      /* receiver clock bias to time systems (s) */
        unsigned char type; /* type (0:xyz-ecef,1:enu-baseline) */
        unsigned char stat; /* solution status (SOLQ_???) */
        unsigned char ns;   /* number of valid satellites */
        float age;          /* age of differential (s) */
        float ratio;        /* AR ratio factor for valiation */
    } sol_t;