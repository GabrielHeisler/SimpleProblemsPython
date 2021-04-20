
#05 - Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

n = int(input("Please, insert a number:"))
sum = 0
for i in range (1, n):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i

print("The sum of the numbers 1 to", n, "is", sum)