from .globals import LAST_NEW_MOON_OF_LAST_YEAR, FRIST_NEW_MOON_OF_NEXT_YEAR, YEAR_DAYS, CYCLES_PER_SOLAR_YEAR, BASE_YEAR, NEW_MOON_OF_JULIAN_JANURY_2000
from .formats import calendarFormat
import juliandate as jd
import math
import numpy as np

def computePhases(year):
    cycle = getCycleEstimate(year, 0)
    calendar = []

    for i in range(LAST_NEW_MOON_OF_LAST_YEAR, FRIST_NEW_MOON_OF_NEXT_YEAR):
        calendar.extend([
            calendarFormat(getPhaseDate(cycle + i, 0), "New"),
            calendarFormat(getPhaseDate(cycle + i, 0.25), "First quarter"),
            calendarFormat(getPhaseDate(cycle + i, 0.5), "Full moon"),
            calendarFormat(getPhaseDate(cycle + i, 0.75), "Last quarter")
        ])

   
    
    return calendar

def mod360(f):
    t=f%360
    
    if t<0:
        t+=360
    
    return t

def getCycleEstimate(year, month):
    yearFrac=(month*30+15)/YEAR_DAYS
    k=CYCLES_PER_SOLAR_YEAR*((year + yearFrac) - BASE_YEAR)
    k=math.floor(k)
    
    return k


def getPhaseDate(cycle, phase): 
    k = cycle+phase
    
    toRad = np.pi / 180
    

    #julian day
    T = k/1236.85 
    JDE = NEW_MOON_OF_JULIAN_JANURY_2000 + 29.530588861*k + 0.00015437*T*T - 0.000000150*T*T*T + 0.00000000073*T*T*T*T
    
    E = 1 - 0.002516*T - 0.0000074*T*T

    
    #corrections
    M = mod360(2.5534 + 29.10535670*k - 0.0000014*T*T - 0.00000011*T*T*T)*toRad
    Mp = mod360(201.5643 + 385.81693528*k + 0.0107582*T*T + 0.00001238*T*T*T - 0.000000058*T*T*T*T)*toRad
    F = mod360(160.7108 + 390.67050284*k - 0.0016118*T*T - 0.00000227*T*T*T + 0.000000011*T*T*T*T)*toRad
    Om = mod360(124.7746 - 1.56375588*k + 0.0020672*T*T + 0.00000215*T*T*T)*toRad

    A1 = mod360(299.77 + 0.107408*k - 0.009173*T*T)*toRad;
    A2 = mod360(251.88 + 0.016321*k)*toRad;
    A3 = mod360(251.83 + 26.651886*k)*toRad;
    A4 = mod360(349.42 + 36.412478*k)*toRad;
    A5 = mod360(84.66 + 18.206239*k)*toRad;
    A6 = mod360(141.74 + 53.303771*k)*toRad;
    A7 = mod360(207.14 + 2.453732*k)*toRad;
    A8 = mod360(154.84 + 7.306860*k)*toRad;
    A9 = mod360(34.52 + 27.261239*k)*toRad;
    A10 = mod360(207.19 + 0.121824*k)*toRad;
    A11 = mod360(291.34 + 1.844379*k)*toRad;
    A12 = mod360(161.72 + 24.198154*k)*toRad;
    A13 = mod360(239.56 + 25.513099*k)*toRad;
    A14 = mod360(331.55 + 3.592518*k)*toRad;

    correction = 0

    if phase == 0:
        correction = 0.00002*math.sin(4*Mp) + -0.00002*math.sin(3*Mp + M) + -0.00002*math.sin(Mp - M - 2*F) + 0.00003*math.sin(Mp - M + 2*F) + \
            -0.00003*math.sin(Mp + M + 2*F) + 0.00003*math.sin(2*Mp + 2*F) + 0.00003*math.sin(Mp + M - 2*F) + 0.00004*math.sin(3*M) + \
            0.00004*math.sin(2*Mp - 2*F) + -0.00007*math.sin(Mp + 2*M) + -0.00017*math.sin(Om) + -0.00024*E*math.sin(2*Mp - M) + 0.00038*E*math.sin(M - 2*F) + \
            0.00042*E*math.sin(M + 2*F) + -0.00042*math.sin(3*Mp) + 0.00056*E*math.sin(2*Mp + M) + -0.00057*math.sin(Mp + 2*F) + -0.00111*math.sin(Mp - 2*F) + \
            0.00208*E*E*math.sin(2*M) + -0.00514*E*math.sin(Mp + M) + 0.00739*E*math.sin(Mp - M) + 0.01039*math.sin(2*F) + 0.01608*math.sin(2*Mp) + \
            0.17241*E*math.sin(M) + -0.40720*math.sin(Mp)
    elif phase == 0.25:
        correction = -0.00002*math.sin(3*Mp + M) + 0.00002*math.sin(Mp - M + 2*F) + 0.00002*math.sin(2*Mp - 2*F) + 0.00003*math.sin(3*M) + \
            0.00003*math.sin(Mp + M - 2*F) + 0.00004*math.sin(Mp - 2*M) + -0.00004*math.sin(Mp + M + 2*F) + 0.00004*math.sin(2*Mp + 2*F) + \
            -0.00005*math.sin(Mp - M - 2*F) + -0.00017*math.sin(Om) + 0.00027*E*math.sin(2*Mp + M) + -0.00028*E*E*math.sin(Mp + 2*M) + \
            0.00032*E*math.sin(M - 2*F) + 0.00032*E*math.sin(M + 2*F) + -0.00034*E*math.sin(2*Mp - M) + -0.00040*math.sin(3*Mp) + -0.00070*math.sin(Mp + 2*F) + \
            -0.00180*math.sin(Mp - 2*F) + 0.00204*E*E*math.sin(2*M) + 0.00454*E*math.sin(Mp - M) + 0.00804*math.sin(2*F) + 0.00862*math.sin(2*Mp) + \
            -0.01183*E*math.sin(Mp + M) + 0.17172*E*math.sin(M) + -0.62801*math.sin(Mp);    
    
        W = 0.00306 - 0.00038*E*math.cos(M) + 0.00026*math.cos(Mp) - 0.00002*math.cos(Mp - M) + 0.00002*math.cos(Mp + M) + 0.00002*math.cos(2*F)

        if phase == 0.25:
            correction += W
        else:
            correction -= W
    
    elif phase == 0.5:
        correction = 0.00002*math.sin(4*Mp) + -0.00002*math.sin(3*Mp + M) + -0.00002*math.sin(Mp - M - 2*F) + 0.00003*math.sin(Mp - M + 2*F) + \
            -0.00003*math.sin(Mp + M + 2*F) + 0.00003*math.sin(2*Mp + 2*F) + 0.00003*math.sin(Mp + M - 2*F) + 0.00004*math.sin(3*M) + \
            0.00004*math.sin(2*Mp - 2*F) + -0.00007*math.sin(Mp + 2*M) + -0.00017*math.sin(Om) + -0.00024*E*math.sin(2*Mp - M) + \
            0.00038*E*math.sin(M - 2*F) + 0.00042*E*math.sin(M + 2*F) + -0.00042*math.sin(3*Mp) + 0.00056*E*math.sin(2*Mp + M) + \
            -0.00057*math.sin(Mp + 2*F) + -0.00111*math.sin(Mp - 2*F) + 0.00209*E*E*math.sin(2*M) + -0.00514*E*math.sin(Mp + M) + \
            0.00734*E*math.sin(Mp - M) + 0.01043*math.sin(2*F) + 0.01614*math.sin(2*Mp) + 0.17302*E*math.sin(M) + -0.40614*math.sin(Mp)

    JDE += correction
    correction = 0.000325*math.sin(A1) + 0.000165*math.sin(A2) + 0.000164*math.sin(A3) + 0.000126*math.sin(A4) + 0.000110*math.sin(A5) + \
        0.000062*math.sin(A6) + 0.000060*math.sin(A7) +0.000056*math.sin(A8) + 0.000047*math.sin(A9) + 0.000042*math.sin(A10) + 0.000040*math.sin(A11) + \
        0.000037*math.sin(A12) + 0.000035*math.sin(A13) + 0.000023*math.sin(A14);
        
    JDE += correction;

    return JDE



