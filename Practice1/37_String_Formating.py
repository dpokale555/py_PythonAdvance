#Example 1:
# numbers = [4,5,6]
# newstring= "Numbers:{0},{1},{2}".format(numbers[0],numbers[1],numbers[2])
# print(newstring)

#Example 2: Print the input date
number=(input().split())
date="{0}/{1}/{2}".format(number[0],number[1],number[2])
print("The input date is :",date)

#Example 3: string format
a="{X}/{Y}".format(X=100,Y=200)
print(a)
