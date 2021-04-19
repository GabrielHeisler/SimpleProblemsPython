import math
#10. 1575 students of a school want to go Agra by bus. If one bus can carry 75 students, how many buses are required to carry all the students?

students = 1575
bus_size = 75

amount = students / bus_size
amount = math.ceil(amount)

print(amount, "buses will be required to carry", students, "students")