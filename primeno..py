number=int(raw_input("enter the number to be checked"))
if number>1:
    for i in range(2,number):
        if number%i==0 :
            print "not prime"
    else:
            print "prime"
else:
    print "not prime"

num = int(raw_input("Enter a number to chk prime or not : "))

# taking the input from the user
# prime numbers are greater than 1, so checking the condition..
if num > 1:
    # checking for factors....
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")  # to execute the loop if condition met ...
            break
    else:
        print(num, "is a prime number")  # entered number is prime number ...

# if input number is less than or equal to 1, it is not prime number....
else:
    print(num, "is not a prime number")