import re

pattern1 = r"Gr.y"

if re.match(pattern1, "Gray"):
    print("Match found")
else:
    print("Match not found")