
#04 - Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

n = int(input("Please, insert a number:"))
sum = 0
for i in range (1, n):
    sum = sum + i

print("The sum of the numbers 1 to", n, "is", sum)