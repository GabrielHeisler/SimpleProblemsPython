
#06 - Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.

n = int(input("Insert a number:"))
choice = "x"
while choice.lower() != "s" and choice.lower() != "p":
    choice = input("Do you want to compute\nThe sum of 1,...,n[PRESS S]\tThe produtct of 1,...,n[PRESS P]")
if choice.lower() == "s":
    sum = 0
    for i in range (1, n):
        sum = sum + i
    print("The sum of 1,...,", n, "is", sum)

elif choice.lower() == "p":
    product = 1
    for i in range (1, n):
        product = product * i
    print("The product of 1,...,", n, "is", product)