#Example 1: filter out the even and odd number from the list
newlist = [1,2,3,4,5,6,7,8,9,11,12,13,14,15]

Even_num=list(filter(lambda x:x%2==0,newlist))
print(Even_num)
Odd_num=list(filter(lambda x:x%2!=0,newlist))
print(Odd_num)
