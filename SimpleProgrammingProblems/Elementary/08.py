
#08 - Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers,
#     printing all primes up to the largest number you can easily represent is fine too.)

#     In this case I printed all prime numbers in an interval.

first= 10
last = 100
for num in range(first, last+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)