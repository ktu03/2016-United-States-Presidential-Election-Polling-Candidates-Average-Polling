from cs103 import *

@typecheck
def crime_type_as_str(ct: CrimeType) -> str:
    """
    Returns a string describing the crime type `ct`.
    """
    # return "" # stub
    
    # template from CrimeType
    if ct == CrimeType.BEC:
        return "Break and Enter Commercial"
    elif ct == CrimeType.BER:
        return "Break and Enter Residential/Other"
    elif ct == CrimeType.TB:
        return "Theft of Bicycle"
    elif ct == CrimeType.TV:
        return "Theft of Vehicle"


start_testing()

expect(crime_type_as_str(CrimeType.BEC), "Break and Enter Commercial")
expect(crime_type_as_str(CrimeType.BER), "Break and Enter Residential/Other")
expect(crime_type_as_str(CrimeType.TB), "Theft of Bicycle")
expect(crime_type_as_str(CrimeType.TV), "Theft of Vehicle")

summary()
    
    
@typecheck
def parse_crime_type(s:str) -> CrimeType:
    """
    Returns the string s as a CrimeType.
    
    Assumes s is one of the following:
        "Break and Enter Commercial"
        "Break and Enter Residential/Other"
        "Theft of Bicycle"
        "Theft of Vehicle"
    """
    # return CrimeType.BEC # stub
    # template from atomic non-distinct
    # return ...(s)
    if s == "Break and Enter Commercial":
        return CrimeType.BEC
    elif s == "Break and Enter Residential/Other":
        return CrimeType.BER
    elif s == "Theft of Bicycle":
        return CrimeType.TB
    elif s == "Theft of Vehicle":
        return CrimeType.TV
    
    
start_testing()

expect(parse_crime_type("Break and Enter Commercial"), CrimeType.BEC)
expect(parse_crime_type("Break and Enter Residential/Other"), CrimeType.BER)
expect(parse_crime_type("Theft of Bicycle"), CrimeType.TB)
expect(parse_crime_type("Theft of Vehicle"), CrimeType.TV)

summary()


@typecheck
def read(filename: str) -> List[CrimeData]:
    """    
    reads information from the specified file 
    and returns a list of crime data.
    
    Rows with missing times (hour and minute are zero)
    are skipped.
    """
    #return []  #stub
    # Template from HtDAP
    # locd contains the result so far
    locd = [] # type: List[CrimeData]

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            # you may not need to store all the strings in the 
            # current row, and you may need to convert some
            # of the strings to other types
            if is_reliable(row):
                cd = CrimeData(parse_crime_type(row[0]), 
                               parse_int(row[4]))
                locd.append(cd)
    
    return locd

@typecheck
def is_reliable(los: List[str]) -> bool:
    """
    Returns True if los is reliable data.
    
    The data is assumed to be unreliable
    if the 4th and 5th items are both "0".
    """
    # return True # stub
    # not using a template
    return los[4] != "0" or los[5] != "0"

start_testing()

TEST_ALL_BEC = [CrimeData(CrimeType.BEC, 6),
                CrimeData(CrimeType.BEC, 18)] # missing data removed

# Examples and tests for read
expect(read('testfile_empty.csv'), [])
expect(read('testfile_all_missing.csv'), [])
expect(read('testfile_all_bec.csv'), TEST_ALL_BEC)

summary()


start_testing()

# Examples and tests for is_reliable
expect(is_reliable(["1", "0", "0", "0", "0", "0"]), False)
expect(is_reliable(["0", "1", "0", "0", "0", "1"]), True)
expect(is_reliable(["0", "0", "1", "0", "1", "0"]), True)
expect(is_reliable(["0", "0", "0", "1", "1", "1"]), True)

summary()
