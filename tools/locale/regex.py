import re
unformat = [
' 2018-10-08 08:00 - 10:00 Seminarium, SF1625 Helklass, SF1625, Q11, Q13, Q15, Q17, Q22, Q26, CELTE1, CINEK1 ID 163046', ' 2018-10-08 10:00 - 12:00 Lektion, HE1036 Helklass, HE1036, Q11, TIELA3, TITEH3-TIEL ID 194641', ' 2018-10-08 15:00 - 17:00 Övning, SF1661, Q11, Q13, Mikael Cronhjort, CLGYM1 ID 173176', ' 2018-10-09 08:00 - 10:00 Kontrollskrivning, KH1123, Q11, Q13, Q22, Maria Malmström, Mats Jansson, TIKED1, TITEH1-TIKE ID 173263', ' 2018-10-09 13:00 - 15:00 Övning, SF1661, Q11, Q13, Mikael Cronhjort, CLGYM1 ID 173177', ' 2018-10-10 10:00 - 12:00 Övning, EJ2301, Q11, Q13, Q15, TELPM1, TIETM1-SENS, TIETM1-SMCS, TSCRM1-ELEM, TSCRM2-ELEM ID 180326', ' 2018-10-10 15:00 - 17:00 Seminarium, DM2573 Helklass, DM2573, Q11, Q13, Daniel Pargman, CMETE3, CMETE3-BVT, CMETE3-CPS, CMETE3-INMT, CMETE3-LJD, CMETE3-TRK ID 181785', ' 2018-10-10 17:00 - 20:00 THS aktivitet, Q11, Q22, Q24, Q26, Q36, JML-workshop  ID 223636', ' 2018-10-11 16:00 - 18:00 Mastermässa, U-huset, BV28A ID 161079', ' 2018-10-11 10:00 - 12:00 Lektion, SF2561 Helklass, SF2561 Helklass, SF2561, SF2561, Q11, Sara Zahedi, TCSCM1-CSSC, TCSCM2-CSSC, TDTNM1, TTMAM2-COMA ID 185873', ' 2018-10-11 13:00 - 15:00 Information, 8XCELTE, Q11, Q13, Samverkansinlärning, CELTE1 ID 167485', ' 2018-10-12 08:00 - 09:00 Seminarium, SG1220 grupp A, SG1220 grupp B, SG1220 grupp C, SG1220, Q11, Q13, Q24, Lisa Prahl Wittberg, CDEPR3-FOR, CDEPR3-INE, CDEPR3-IPDE, CDEPR3-IPUA, CDEPR3-IPUB, CDEPR3-MRS, CDEPR3-SUE, CDEPR3-SUT, CDEPR3-TEMA, CDEPR3-TEMB, CDEPR3-TEMC, CENMI3-HSS, CENMI3-MES, CENMI3-RENE, CENMI3-SMCS, CENMI3-SUE, CENMI3-SUT, CMAST3-AEE, CMAST3-FOR, CMAST3-INE, CMAST3-IPDE, CMAST3-IPUA, CMAST3-IPUB, CMAST3-IPUC, CMAST3-ITSY, CMAST3-MRS, CMAST3-MTH, CMAST3-NEE, CMAST3-PRM, CMAST3-SUE, CMAST3-SUT, CMAST3-TEMA, CMAST3-TEMB, CMAST3-TEMC, TTEMM1-TEMA, TTEMM2-TEMB ID 175436', ' 2018-10-12 09:00 - 10:00 Seminarium, SG1220 grupp D, SG1220 grupp E, SG1220 grupp F, SG1220, Q11, Q13, Q24, Lisa Prahl Wittberg, CDEPR3-FOR, CDEPR3-INE, CDEPR3-IPDE, CDEPR3-IPUA, CDEPR3-IPUB, CDEPR3-MRS, CDEPR3-SUE, CDEPR3-SUT, CDEPR3-TEMA, CDEPR3-TEMB, CDEPR3-TEMC, CENMI3-HSS, CENMI3-MES, CENMI3-RENE, CENMI3-SMCS, CENMI3-SUE, CENMI3-SUT, CMAST3-AEE, CMAST3-FOR, CMAST3-INE, CMAST3-IPDE, CMAST3-IPUA, CMAST3-IPUB, CMAST3-IPUC, CMAST3-ITSY, CMAST3-MRS, CMAST3-MTH, CMAST3-NEE, CMAST3-PRM, CMAST3-SUE, CMAST3-SUT, CMAST3-TEMA, CMAST3-TEMB, CMAST3-TEMC, TTEMM1-TEMA, TTEMM2-TEMB ID 175438', ' 2018-10-12 10:00 - 12:00 Seminarium, DM2573 Helklass, DM2573, Q11, Q13, Daniel Pargman, CMETE3, CMETE3-BVT, CMETE3-CPS, CMETE3-INMT, CMETE3-LJD, CMETE3-TRK ID 181786'
]

def format_schedule(unformat):
    date = []
    time = []
    for uf in unformat:
        day = re.sub(r'.*(\d\d\d\d-\d\d-\d\d) \d\d:\d\d - \d\d:\d\d.*', r'\1', uf)
        period = re.sub(r'.*\d\d\d\d-\d\d-\d\d (\d\d):\d\d - (\d\d):\d\d.*', r'\1\2', uf)
        #f = re.sub(r'\' (\d\d\d\d-\d\d-\d\d \d\d:\d\d - \d\d:\d\d).*\'', r'\1' , uf)
        date.append(day)
        time.append(period)
    return date, time
# This function will, given the two vector:
# dateVector This has all dates that has something scheduled).
# timeVector This has the start and end times (on a specific format: concat(startTime, endTime)) of each event.
# One find a bijection with the elements which fulfills: dateVector[i] ---> timeVector[i], event on day dateVector[i] starts at time timeVector[i].
def group_daily_schedule(dateVector, timeVector):
    daily = []
    temp = []
    index = 1
    jndex = 0
    # This will basically find the bijection and group each element of timeVector accordingly.
    while index < len(dateVector):
        previous = index-1
        temp.append(timeVector[jndex])
        if dateVector[previous] != dateVector[index]:
            daily.append(temp)
            temp = []
        index += 1
        jndex += 1
    return daily

date, time = format_schedule(unformat)
daily = group_daily_schedule(date, time)
print(daily)
