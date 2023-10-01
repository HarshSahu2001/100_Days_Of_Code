student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

Height_Sum = 0
Student_count = 0
for height in student_heights:
    Height_Sum += height
    Student_count +=1

Average = (Height_Sum/Student_count)
print(int(round(Average, 0)))

# 2nd method:
# Total_Height = sum(student_heights)
# students = len(student_heights)
# Average = Total_Height/students
# print (int(round(Average)))
