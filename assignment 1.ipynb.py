print("Average Calculator of 3 Numbers")
num_1=int(input("Enter the First Number:"))
num_2=int(input("Enter the Second Number:"))
num_3=int(input("Enter the Third Number:"))
average=(num_1+num_2+num_3)/3
print("Average is",round(average,3))

print("______________________________________")
print("\nIncome tax Computation")

tax_rate=20/100
s_d=10000
d_d=3000
gross_income=int(input("Please Enter your Gross Income:"))
num_of_dependents=int(input("Plese Enter the Number of dependents:"))

dependents_deduction=num_of_dependents * d_d
taxable_income=gross_income - s_d - dependents_deduction
tax=taxable_income * tax_rate
print("Your Taxable income is:",taxable_income)
print("Your Tax is:",tax)

print("______________________________________")
print("\nStore Values in a list")
student=[]
sid=int(input("Write your SID:"))
student.append(sid)
name=input("Enter Your Name:")
student.append(name)
gender=input("Enter your Gender:")
student.append(gender)
course_name=input("Enter your Course Name:")
student.append(course_name)
cgpa=input("Please Enter Your CGPA:")
student.append(float(cgpa))
print(student)

print("______________________________________")
print("\nStore Marks Of 5 Students")
list1={}
marks1=int(input("Enter marks of student 1:"))
marks2=int(input("Enter marks of student 2:"))
marks3=int(input("Enter marks of student 3:"))
marks4=int(input("Enter marks of student 4:"))
marks5=int(input("Enter marks of student 5:"))
list1["Marks of First Student"]=marks1
list1["Marks of Second Student"]=marks2
list1["Marks of Third Student"]=marks3
list1["Marks of Fourth Student"]=marks4
list1["Marks of Fifth Student"]=marks5
print(list1)

print("______________________________________")
print("\nPlaying with colors")
colors=["Red","Green","White","Black","Pink","Yellow"]
print(colors)
colors.remove(colors[3])
print(colors)

colors[3]="Purple"
print(colors)

