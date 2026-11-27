no_of_subjects=int(input("Enter The Number of Subjects : "))
marks=[]

for i in range(no_of_subjects):
    sub=input(f"Enter the Name of Subject {i+1}: ")
    m=int(input(f"Enter the marks in {sub} : "))
    marks.append(m)

#AVERAGE MARKS

total = sum(marks)
print("Total Marks = ",total)
avg_marks = total/no_of_subjects
print(f"Average in {no_of_subjects} Subjects = ",avg_marks)

#PASS / FAIL
if avg_marks<40:
    print("FAIL")
else:
    print("PASS")
