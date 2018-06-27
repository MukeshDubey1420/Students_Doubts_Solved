from termcolor import colored                                # Importing Term color to make text colored....

print (colored("<----- Hello! Let's get started ----->","green") )   # Printing hello to start application-->
print (colored('|*****************************|',"blue"))
print (colored('We Welcomes you to Our Introduction Application..!',"blue"))
print ('|*****************************|')
print ('Featuring the Basic Project for introduction..')
print ('|*****************************|')
print ('Designed By Mukesh Dubey..')
print ('|*****************************|')
print ('<---- :Please Enter Your gender: ----->')
gender = input(colored('If You are Male Plz Write "M or m" and "F or f " for Female:',"blue"))
if len(gender)>= 1 and gender.isalpha():
    if gender.upper() == "M":
        print(colored('Hello Sir,, We Welcomes you on Board ...',"green"))
        Name = input("What is Your Good Name : ")
        if len(Name) >= 3 and Name.isalpha():
            print("Hii Sir, Your Name is " + Name)
            print()
            print("I Would Like to collect some more information About You")
            age = int(input(colored("Enter your age (Eligibility criteria is more than 20) ? ", 'blue')))
            if age > 20:
                print("welcome " + str(Name) + " sir, as your age is " + str(age) + " Years,You are elligible for Python Fundamental Course ....")
            else:
                print(colored('You are Under age to enroll for Python Fundamental course', 'red'))
        else:
            print(colored('Name Must be in Alphabets and Greater than 3 characters.and Try Again',"red"))
    elif gender.upper() == "F":
        print('Hello Mam,, We Welcomes you on Board ...')
        Name = input("What is Your Good Name : ")
        if len(Name) >= 4 and Name.isalpha():
            print("Hii Mam, Your Name is " + Name)
            print()
            print("I Would Like to collect some more information About You")
            age = int(input(colored("Enter your age (Eligibility criteria is more than 19) ? ", 'blue')))
            if age > 19:
                print("welcome " + str(Name) + " Mam, as your age is " + str(age) + " Years,You are elligible for Core Java Fundamental Course ....")
            else:
                print(colored('You are Under age to enroll for Core Java Fundamental course', 'red'))
        else:
            print(colored('Name Must be in Alphabets and Greater than 4 characters.and Try Again',"red"))
    else:
        print("Provide Only M for Male And F for Female..and Try Again")
else:
    print("please enter the valid input (M OR F) and Try Again")

