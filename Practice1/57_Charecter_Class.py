import re
#Example 1:
patter1 = r"[A-Z][]A-Z][0-9]"

if re.search(patter1,"AH9"):
    print("Match Found")

#Eaxmple 2:
license_plate=r"[A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9][0-9]"

if re.search(license_plate,"MH14DG2345"):
    print("Match found2")

