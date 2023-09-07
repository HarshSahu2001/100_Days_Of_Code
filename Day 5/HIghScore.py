student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
     highest_score = score
print(f"The highest score in the class is: {highest_score}")

# Method 2
# Sorted_Score = sorted(student_scores)
# Highest = Sorted_Score[len(Sorted_Score)-1]
# print(f"The highest score in the class is: {Highest}")

# Method 3
# highest = max(student_scores)
# print(f"The highest score in the class is: {highest}")

# lowest = min(student_scores)
# print(f"The lowest score in the class is: {lowest}")
