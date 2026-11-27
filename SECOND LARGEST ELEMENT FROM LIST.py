n=int(input("Enter Number of Elements : "))
mylist=[]
for i in range(n):
    x=int(input("Enter Element : "))
    mylist.append(x)
print("List = ", mylist)
print("Initial Largest Element = ",max(mylist))
no_duplicates = list(set(mylist))
no_duplicates.remove(max(no_duplicates))
print("Second Largest Element = ", max(no_duplicates))


