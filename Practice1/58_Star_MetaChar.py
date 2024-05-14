import re

pattern1 = r"eggs(bacon)*"

if re.match(pattern1,"eggs"):
    print("match found1")

if re.match(pattern1,"eggsbeacon"):
    print("match found2")

if re.match(pattern1,"eggsbeaconbeacon"):
    print("match found3")

if re.match(pattern1,"beacon"):
    print("match found4")