import re

pattern = r"eggs"

if re.match(pattern,"rdytfeggsjghkeggs"):
    print("Mathc Found1")
else:
    print("No match found1")

if re.match(pattern,"rdytfeggsjghk"):
    print("Mathc Found2")
else:
    print("No match found2")

if re.match(pattern,"rdytfjghkeggs"):
    print("Mathc Found3")
else:
    print("No match found3")

if re.match(pattern,"eggsrdytfjghk"):
    print("Mathc Found4")
else:
    print("No match found4")