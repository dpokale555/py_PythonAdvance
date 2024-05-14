import re

string1="My name is Ram, Hi I am ram"
pattern1= r"Ram"
newstring1=re.sub(pattern1,"Shyam", string1)
print(newstring1)