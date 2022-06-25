n = int(input("Enter a number which contains 5 digits: "))
a = 0

a = a + n % 10
n = n // 10

a = a + n % 10
n = n // 10

a = a + n % 10
n = n // 10

a = a + n % 10
n = n // 10

a = a + n % 10
n = n // 10

print("The total of 5 digits is: ", a)
