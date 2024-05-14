import re

pattern1 =r"^gr.y$"          #^: To confirm the starting of string and $: to confirm the ending of the string

if re.match(pattern1,"gray"):
    print("Match Found 1")
else:
    print("Match Not found 1")

if re.match(pattern1,"tray"):
    print("Match Found 1")
else:
    print("Match Not found 1")

if re.match(pattern1,"grap"):
    print("Match Found 1")
else:
    print("Match Not found 1")