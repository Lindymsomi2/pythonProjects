mark = int(input("Enter your mark: "))

if mark >= 90 and mark <=100:
    print("Grade A")   
elif mark >=70 and mark <=89:
    print("Grade B")
elif mark >=60 and mark <=69:
    print("Grade C")
elif mark >=50 and mark <=59:
    print("Grade D")
elif mark <50 and mark >0:
    print("Grade F")
else: 
    print("Invalid mark")