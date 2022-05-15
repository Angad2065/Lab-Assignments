print("_________________________________________________________________________________")
print("Program 1")
str1="Python is a case sensitive language"
print(str1)
#For a part
print(len(str1))
#for b part
print(str1[::-1])
#for c part
new_string=str1[10:26]
print(new_string)
#for d part
print(str1.replace("a case sensitive","object oriented"))
#for e part
print(str1.replace(" ",""))


print("_________________________________________________________________________________")
print("Program 2")
name="Angad"
sid=21102065
branch="Civil"
cgpa=9.9
print("Hey, {} Here!".format(name))
print("My SID is {}".format(sid))
print("I am from {} department and my CGPA is {}".format(branch,cgpa))

print("_________________________________________________________________________________")
print("Program 3")
a=56
b=10
#3a
print(a&b)
#3b
print(a|b)
#3c
print(a^b)
#3d
print(a<<2)
print(b<<2)
#3e
print(a>>2)
print(b>>4)

print("_________________________________________________________________________________")
print("Program 4")
str2=input("Enter the Desired String: ")
if "name" in str2:
    print("Yes")
else:
    print("No")

print("_________________________________________________________________________________")
print("Program 5")
a=int(input("Enter the 1st length: "))
b=int(input("Enter the 2nd length: "))
c=int(input("Enter the 3rd length: "))
if a<b+c and b<c+a and c<a+b:
    print("Yes")
else:
    print("No")

print("_________________________________________________________________________________")
print("Program 6")
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
num=a^b
Count_flipped_bit=0
while(num!=0):
    num=num&(num-1)
    Count_flipped_bit+=1
print("Number of bits needed to be flipped to convert a to b is:",Count_flipped_bit)
