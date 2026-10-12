# list of student names
students = ["Melissa", "Daisy", "Michael", "Thabo", "Sarah"]
# list of marks
marks = [78, 62, 92, 55, 85, 76]

# tuple
subjects = ("Python", "JavaScript", "HTML")

# dictionary
student_details = {
    "name": "Melissa",
    "age": 21,
    "grade": "B"
}
# lists, indexing and slicing
print(students[0])
print(students[-1])
print(students[0:3])
print(marks[-2: : 1])

# add another student to end of list
students.append("Ashley")
students.insert(1,"Alex")
# remove thabo from list
students.remove("Thabo")
marks.sort()
marks.reverse()
print(marks)
print(students)
num = len(students)
print(num)


# forloops
for i in range(num):
    print("%s scored %d" %(students[i], marks[i]))
    

#total of all the marks
total = 0
for i in marks:
    total += i  
    
print(total)

#average of all the marks
avg = 0
for i in marks:
    avg += i  / len(marks)
    
print(avg)

# print numbers from 1 to 5
count = 1

while count <=5:
    print(count)
    count+=1 
  
# count the marks above 70 
gradeA = 0 
for i in marks:
    if i >= 70:
        gradeA+=1
print("Number of marks above 70 is",gradeA) 