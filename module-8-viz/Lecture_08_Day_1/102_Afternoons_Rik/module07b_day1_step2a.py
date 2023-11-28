from cs103 import *
from typing import NamedTuple, List
import csv
from enum import Enum

##################
# Data Definitions


CrimeType = Enum('CrimeType', 
                 ['BEC', 'BER', 'TV', 'TB'])

#interp. A crime type, one of:
#    BNE Commercial (BEC)
#    BNE Residential/Other (BER)
#    Theft of Vehicle (TV)
#    Theft of Bicycle (TB)

# examples are redundant for enumerations

# template based on enumeration (4 cases)
@typecheck
def fn_for_crime_type(ct: CrimeType) -> ...:
    if ct == CrimeType.BEC:
        return ...
    elif ct == CrimeType.BER:
        return ...
    elif ct == CrimeType.TV:
        return ...
    elif ct == CrimeType.TB:
        return ...
    

CrimeData = NamedTuple('CrimeData',
                       [('type', CrimeType),
                        ('hour', int)]) # in range [0,23]

# interp. Data about a crime, including 
# the type of crime and the hour it occurred

CD1 = CrimeData(CrimeType.BEC, 0)
CD2 = CrimeData(CrimeType.BER, 23)
CD3 = CrimeData(CrimeType.TV, 8)
CD4 = CrimeData(CrimeType.TB, 16)

# template based on compound (2 fields)
# and reference rule
@typecheck
def fn_for_crime_data(cd: CrimeData) -> ...:
    return ...(fn_for_crime_type(cd.type), cd.hour)


# List[CrimeData]
# interp. a list of CrimeData

LOCD0 = []
LOCD1 = [CD1]
LOCD2 = [CD1, CD2, CD3, CD4]

# template based on arbitrary-sized and reference rule
@typecheck
def fn_for_locd(locd: List[CrimeData]) -> ...:
    # description of the accumulator
    acc = ...      # type: ...
    for cd in locd:
        acc = ...(fn_for_crime_data(cd), acc)
    return ...(acc)


# Here are some definitions we'll need later on that 
# aren't particularly interesting to work on in class!

# List[str]
# interp. a list of strings
LOS0 = []
LOS1 = ['hello', 'world']

# template based on arbitrary-sized data
@typecheck
def fn_for_los(los: List[str]) -> ...:
    # description of accumulator
    acc = ... # type: ...
    
    for s in los:
        acc = ...(s, acc)
        
    return ...(acc)


# List[int]
# interp. a list of integers
LOI0 = []
LOI1 = [1, -12]

# template based on arbitrary-sized data
@typecheck
def fn_for_loi(loi: List[int]) -> ...:
    # description of accumulator
    acc = ... # type: ...
    
    for i in loi:
        acc = ...(i, acc)
        
    return ...(acc)

