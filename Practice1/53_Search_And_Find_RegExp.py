import re

pattern = r"eggs"

#Example 1: for search
if re.search(pattern,"rdytfeggsjghkeg"):
    print("Mathc Found1")
else:
    print("No match found1")\

if re.search(pattern,"rdytfjghkeggs"):
    print("Mathc Found2")
else:
    print("No match found2")

#Example 2: findall
if re.findall(pattern, "rdytfjghkeggs"):
    print("Mathc Found3")
else:
    print("No match found3")

#Example3: findall in one line
print(re.findall(pattern,"rdytfjghkeggsjgvjvgeggsvghv"))

