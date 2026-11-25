n=int(input("Enter Number of Elements : "))
mylist=[]
for i in range(n):
    x=int(input("Enter Element : "))
    mylist.append(x)
print("List = ", mylist)
print("Maximum Element in List = ",max(mylist))
print("Minimum Element in List = ",min(mylist))
