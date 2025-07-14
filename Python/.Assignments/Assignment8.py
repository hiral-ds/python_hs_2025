students = {"Shreya": 85, "Rhea": 90, "Janvi": 78}

students["David"] = 95

average = sum(students.values()) / len(students)
print("Average Grade:", average)

topper = max(students, key=students.get)
print("Top Performer:", topper, "with", students[topper])