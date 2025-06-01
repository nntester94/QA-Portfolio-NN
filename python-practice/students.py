from classes import student

student1 = student("Sam" ,"year 2", "Art", "4.2")
student2 = student("Pam" ,"year 3", "sci", "3.2")
student3 = student("dam" ,"year 2", "Art", "4.2")
student4 = student("fam" ,"year 1", "Art", "4.3")
student5 = student("jam" ,"year 3", "biz", "3.2")
student6 = student("bam" ,"year 2", "sci", "4.7")

students = [student1,student2,student3,student4,student5,student6]

for student in students:
    if student.major == "Art":
        print(f'Student Name: {student.name}, Student Age: {student.year}')

print(student2)