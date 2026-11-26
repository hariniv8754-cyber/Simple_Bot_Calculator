def average(Student):
    Total = 0
    for i in Student:
        Total += i
    avg = Total/len(Student)
    return avg
n = int(input("Enter The Number Of Students:"))
Students = []
for i in range(n):
    S = list(map(int, input().split()))
    print("Average:",average(S))
    Students.append(average(S))
print("The Average of all students is :",average(Students))