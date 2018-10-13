import pandas as pd
import re

# test inputs
relevantRooms = ["Q11", "Q13", "Q15", "Q17", "Q21", "Q22", "Q24", "Q26", "Q31", "Q33", "Q34", "Q36"]

noform0 = [' 2018-10-08 08:00 - 10:00 Seminarium, SF1625 Helklass, SF1625, Q11, Q13, Q15, Q17, Q22, Q26, CELTE1, CINEK1 ID 163046', ' 2018-10-08 10:00 - 12:00 Lektion, HE1036 Helklass, HE1036, Q11, TIELA3, TITEH3-TIEL ID 194641', ' 2018-10-08 15:00 - 17:00 Övning, SF1661, Q11, Q13, Mikael Cronhjort, CLGYM1 ID 173176', ' 2018-10-09 08:00 - 10:00 Kontrollskrivning, KH1123, Q11, Q13, Q22, Maria Malmström, Mats Jansson, TIKED1, TITEH1-TIKE ID 173263', ' 2018-10-09 13:00 - 15:00 Övning, SF1661, Q11, Q13, Mikael Cronhjort, CLGYM1 ID 173177', ' 2018-10-10 10:00 - 12:00 Övning, EJ2301, Q11, Q13, Q15, TELPM1, TIETM1-SENS, TIETM1-SMCS, TSCRM1-ELEM, TSCRM2-ELEM ID 180326', ' 2018-10-10 15:00 - 17:00 Seminarium, DM2573 Helklass, DM2573, Q11, Q13, Daniel Pargman, CMETE3, CMETE3-BVT, CMETE3-CPS, CMETE3-INMT, CMETE3-LJD, CMETE3-TRK ID 181785', ' 2018-10-10 17:00 - 20:00 THS aktivitet, Q11, Q22, Q24, Q26, Q36, JML-workshop  ID 223636', ' 2018-10-11 16:00 - 18:00 Mastermässa, U-huset, BV28A ID 161079', ' 2018-10-11 10:00 - 12:00 Lektion, SF2561 Helklass, SF2561 Helklass, SF2561, SF2561, Q11, Sara Zahedi, TCSCM1-CSSC, TCSCM2-CSSC, TDTNM1, TTMAM2-COMA ID 185873', ' 2018-10-11 13:00 - 15:00 Information, 8XCELTE, Q11, Q13, Samverkansinlärning, CELTE1 ID 167485', ' 2018-10-12 08:00 - 09:00 Seminarium, SG1220 grupp A, SG1220 grupp B, SG1220 grupp C, SG1220, Q11, Q13, Q24, Lisa Prahl Wittberg, CDEPR3-FOR, CDEPR3-INE, CDEPR3-IPDE, CDEPR3-IPUA, CDEPR3-IPUB, CDEPR3-MRS, CDEPR3-SUE, CDEPR3-SUT, CDEPR3-TEMA, CDEPR3-TEMB, CDEPR3-TEMC, CENMI3-HSS, CENMI3-MES, CENMI3-RENE, CENMI3-SMCS, CENMI3-SUE, CENMI3-SUT, CMAST3-AEE, CMAST3-FOR, CMAST3-INE, CMAST3-IPDE, CMAST3-IPUA, CMAST3-IPUB, CMAST3-IPUC, CMAST3-ITSY, CMAST3-MRS, CMAST3-MTH, CMAST3-NEE, CMAST3-PRM, CMAST3-SUE, CMAST3-SUT, CMAST3-TEMA, CMAST3-TEMB, CMAST3-TEMC, TTEMM1-TEMA, TTEMM2-TEMB ID 175436', ' 2018-10-12 09:00 - 10:00 Seminarium, SG1220 grupp D, SG1220 grupp E, SG1220 grupp F, SG1220, Q11, Q13, Q24, Lisa Prahl Wittberg, CDEPR3-FOR, CDEPR3-INE, CDEPR3-IPDE, CDEPR3-IPUA, CDEPR3-IPUB, CDEPR3-MRS, CDEPR3-SUE, CDEPR3-SUT, CDEPR3-TEMA, CDEPR3-TEMB, CDEPR3-TEMC, CENMI3-HSS, CENMI3-MES, CENMI3-RENE, CENMI3-SMCS, CENMI3-SUE, CENMI3-SUT, CMAST3-AEE, CMAST3-FOR, CMAST3-INE, CMAST3-IPDE, CMAST3-IPUA, CMAST3-IPUB, CMAST3-IPUC, CMAST3-ITSY, CMAST3-MRS, CMAST3-MTH, CMAST3-NEE, CMAST3-PRM, CMAST3-SUE, CMAST3-SUT, CMAST3-TEMA, CMAST3-TEMB, CMAST3-TEMC, TTEMM1-TEMA, TTEMM2-TEMB ID 175438', ' 2018-10-12 10:00 - 12:00 Seminarium, DM2573 Helklass, DM2573, Q11, Q13, Daniel Pargman, CMETE3, CMETE3-BVT, CMETE3-CPS, CMETE3-INMT, CMETE3-LJD, CMETE3-TRK ID 181786']

noform1 = [' 2018-10-08 08:00 - 10:00 Seminarium, SF1625 Helklass, SF1625, Q11, Q13, Q15, Q17, Q22, Q26, CELTE1, CINEK1 ID 163046', ' 2018-10-08 15:00 - 17:00 Övning, SF1661, Q11, Q13, Mikael Cronhjort, CLGYM1 ID 173176', ' 2018-10-09 08:00 - 10:00 Kontrollskrivning, KH1123, Q11, Q13, Q22, Maria Malmström, Mats Jansson, TIKED1, TITEH1-TIKE ID 173263', ' 2018-10-09 13:00 - 15:00 Övning, SF1661, Q11, Q13, Mikael Cronhjort, CLGYM1 ID 173177', ' 2018-10-09 15:00 - 17:00 Övning, EQ2415, Q13, TEBSM2-INMV, TEBSM2-INSR, TINNM2, TINNM2-INF, TINNM2-MMB, TIVNM2-DMTE, TMLEM2 ID 194389', ' 2018-10-10 10:00 - 12:00 Övning, EJ2301, Q11, Q13, Q15, TELPM1, TIETM1-SENS, TIETM1-SMCS, TSCRM1-ELEM, TSCRM2-ELEM ID 180326', ' 2018-10-10 13:00 - 15:00 Övning, SF1625 Helklass, SF1625, B1, Q13, Q15, Q17, Q22, Q26, CELTE1, CINEK1 ID 163051', ' 2018-10-10 15:00 - 17:00 Seminarium, DM2573 Helklass, DM2573, Q11, Q13, Daniel Pargman, CMETE3, CMETE3-BVT, CMETE3-CPS, CMETE3-INMT, CMETE3-LJD, CMETE3-TRK ID 181785', ' 2018-10-10 17:00 - 20:00 THS aktivitet, Q13, Workshop för medlemmarna om bilder  och bildteknik ID 234477', ' 2018-10-11 16:00 - 18:00 Mastermässa, U-huset, BV28A ID 161079', ' 2018-10-11 08:00 - 12:00 Övning, AI1144 Helklass, AI1144, Q13, Q17, TFAFK2, TFOFK2 ID 176759', ' 2018-10-11 13:00 - 15:00 Information, 8XCELTE, Q11, Q13, Samverkansinlärning, CELTE1 ID 167485', ' 2018-10-12 08:00 - 09:00 Seminarium, SG1220 grupp A, SG1220 grupp B, SG1220 grupp C, SG1220, Q11, Q13, Q24, Lisa Prahl Wittberg, CDEPR3-FOR, CDEPR3-INE, CDEPR3-IPDE, CDEPR3-IPUA, CDEPR3-IPUB, CDEPR3-MRS, CDEPR3-SUE, CDEPR3-SUT, CDEPR3-TEMA, CDEPR3-TEMB, CDEPR3-TEMC, CENMI3-HSS, CENMI3-MES, CENMI3-RENE, CENMI3-SMCS, CENMI3-SUE, CENMI3-SUT, CMAST3-AEE, CMAST3-FOR, CMAST3-INE, CMAST3-IPDE, CMAST3-IPUA, CMAST3-IPUB, CMAST3-IPUC, CMAST3-ITSY, CMAST3-MRS, CMAST3-MTH, CMAST3-NEE, CMAST3-PRM, CMAST3-SUE, CMAST3-SUT, CMAST3-TEMA, CMAST3-TEMB, CMAST3-TEMC, TTEMM1-TEMA, TTEMM2-TEMB ID 175436', ' 2018-10-12 09:00 - 10:00 Seminarium, SG1220 grupp D, SG1220 grupp E, SG1220 grupp F, SG1220, Q11, Q13, Q24, Lisa Prahl Wittberg, CDEPR3-FOR, CDEPR3-INE, CDEPR3-IPDE, CDEPR3-IPUA, CDEPR3-IPUB, CDEPR3-MRS, CDEPR3-SUE, CDEPR3-SUT, CDEPR3-TEMA, CDEPR3-TEMB, CDEPR3-TEMC, CENMI3-HSS, CENMI3-MES, CENMI3-RENE, CENMI3-SMCS, CENMI3-SUE, CENMI3-SUT, CMAST3-AEE, CMAST3-FOR, CMAST3-INE, CMAST3-IPDE, CMAST3-IPUA, CMAST3-IPUB, CMAST3-IPUC, CMAST3-ITSY, CMAST3-MRS, CMAST3-MTH, CMAST3-NEE, CMAST3-PRM, CMAST3-SUE, CMAST3-SUT, CMAST3-TEMA, CMAST3-TEMB, CMAST3-TEMC, TTEMM1-TEMA, TTEMM2-TEMB ID 175438', ' 2018-10-12 10:00 - 12:00 Seminarium, DM2573 Helklass, DM2573, Q11, Q13, Daniel Pargman, CMETE3, CMETE3-BVT, CMETE3-CPS, CMETE3-INMT, CMETE3-LJD, CMETE3-TRK ID 181786', ' 2018-10-12 13:00 - 15:00 Övning, SF1625 Helklass, SF1625, Q13, Q15, Q17, Q22, Q26, V2, CELTE1, CINEK1 ID 163052']


'''
This function will format the output from the selenuiumscraping of title-attribute. The event name.
I only want to keep the date and the starttime endtime.
args:
dframe      The DataFrame that I will append to.
unformat    The unformatted data/strings/array.
room        The room for this unformatted data. I need this to map correctly in the DataFrame.
'''
def format_schedule(dframe, unformat, room):
    for uf in unformat:
        # The title has a lot of fluff that we are not interested in. This is formatted with regex.
        day = re.sub(r'.*(\d\d\d\d-\d\d-\d\d) \d\d:\d\d - \d\d:\d\d.*', r'\1', uf)
        period = re.sub(r'.*\d\d\d\d-\d\d-\d\d (\d\d):\d\d - (\d\d):\d\d.*', r'\1\2', uf)
        #f = re.sub(r'\' (\d\d\d\d-\d\d-\d\d \d\d:\d\d - \d\d:\d\d).*\'', r'\1' , uf)
        #print(day, period)
        temp = pd.DataFrame({'room': [room], 'date': [day], 'hour': [period]})
        dframe = dframe.append(temp)
    return dframe

# This will return the full DataFrame of formatted data, of scheduled events.
def get_full_frame():
    superFrame = pd.DataFrame(columns=['room', 'date', 'hour'])
    superFrame = format_schedule(superFrame, noform0, "Q11")
    superFrame = format_schedule(superFrame, noform0, "Q13")
    return superFrame
