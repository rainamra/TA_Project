def convertToRadians(degrees):
     return(degrees * 3.14 / 180)

degrees = 150
radians = convertToRadians(degrees)
print ("Degrees :",degrees)
print ("Radians :",radians)

student1 = 80.0
student2 = 90.0
student3 = 66.5
student_scores = [80.0, 90.0, 66.5]
print("Student scores:")
for student_scores in student_scores:
    print(student_scores)
average = (student1 + student2 + student3)/3
print("Average:", average)

class1 = 32
class2 = 45
class3 = 51
member1 = class1 // 5
member2 = class2// 7
member3 = class3 //6
print("Number of students in each group:")
print("Class 1:", member1)
print("Class 2:", member2)
print("Class 3:", member3)
leftover1 = 32 % 5
leftover2 = 45 % 7
leftover3 = 51 % 6
print("Number of students leftover:")
print("Class 1:", leftover1)
print("Class 2:", leftover2)
print("Class 3:", leftover3)

def convertToCirumference (pie_radius):
    return (2 * pi * pie_radius)
pi = 3.14
pie_diameter = 55.4
pie_radius = pie_diameter / 2
circumference_msg = "Jimmy’s pie has a circumference:"
circumference = convertToCirumference (pie_radius)
print(circumference_msg, circumference)

def convertToWavelength (frequency):
    return (speed/frequency)

meters = 20580
speed = meters / 60
frequency = 256
wavelength = convertToWavelength (frequency)

print("The speed (m/s):", speed)
print("The frequency (Hz):", frequency)
print("The wavelength (m):", wavelength)


