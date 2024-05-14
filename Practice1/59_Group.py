import re

pattern1 = r"bread(eggs)*bread"

if re.match(pattern1,"breadbread"):
    print("Match found1")

if re.match(pattern1,"breadeggsbread"):
    print("Match found2")

if re.match(pattern1,"breadeggseggseggsbread"):
    print("Match found3")