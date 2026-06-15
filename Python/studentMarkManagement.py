'''Requirements:
Scenario Question: Student Mark Management System
You are developing a simple Student Mark Management System.
Requirements
    Store marks of 5 students in a list.
    Display all marks.
    Calculate the total marks.
    Calculate the average mark.
    Find the highest mark.
    Find the lowest mark.
    Display whether each student has Passed or Failed.
    Pass mark = 40
    Count how many students passed and failed.'''

# Get the total number of students
n=int(input("Enter the number of students: "))
names=[]
marks=[]

# Get the student names and marks

for i in range(n):
    name=input(f"Enter the name of the student {i+1}: ")
    mark=int(input(f"Enter the mark of the student {i+1}: "))
    names.append(name)
    marks.append(mark)

# Display as list
print("------------------ Display as list -------------------------")
print(names)
print(marks)
print("-------------------------------------------------------------")

# Display in formatting
print("------------------- Display in order ------------------------")
for i in range(n):
    print(names[i],":",marks[i])
print("-------------------------------------------------------------")

# Total and average
total=0
for i in range(n):
    total+=marks[i]
#OR
t=sum(marks)
avg=total/n

# Copy the list
markSort=marks.copy()
markSort.sort(reverse=True)

# Result
print("------------------- Summary ------------------------")
print("Total marks: ", total)
print("Average marks: ", avg)
print("Highest mark: ", markSort[0])
print("Lowest marks: ",markSort[n-1])
print("----------------------------------------------------")
 
 # Pass or Fail
pass_count=0
fail_count=0
pass_students_name=[]
fail_students_name=[]
pass_students_mark=[]
fail_students_mark=[]

for i in range(n):
    if(marks[i]>=40):
        pass_count+=1
        pass_students_name.append(names[i])
        pass_students_mark.append(marks[i])
    else:
        fail_count+=1
        fail_students_name.append(names[i])
        fail_students_mark.append(marks[i])

# Display passed and failed students
print("Passed student : ", pass_count)
print("failed student: ", fail_count)
print("-------------- Passed students --------------------")
for i in range(pass_count):
    print(pass_students_name[i],":",pass_students_mark[i])

print("------------- Failed students -------------------")
for i in range(fail_count):
    print(fail_students_name[i],":",fail_students_mark[i])

print("_______________________________________________________")







       


        










    



