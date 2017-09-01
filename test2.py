spy_name=raw_input("what is your name :")
#concatination of salutation and name
#check weather spy has input something or not
if len(spy_name)>0 and spy_name.isalpha():
    spy_age=0
    spy_rating=0.0
    spy_is_online=False
    spy_slautation = raw_input("what should we call you MR. or Miss ? :")
    if spy_slautation.isalpha():
        spy_name = spy_slautation + " " + spy_name
        print "welcome " + spy_name + " glad to have you back with us"
        print "Alright " + spy_name + " let us know more about you "
        spy_age = int(raw_input("Enter your age:"))
        print"thanks for you input"
        if spy_age > 12 and spy_age < 50:
            print "You are Eligible to be a spy.."

            spy_rating = raw_input("What is your spy rating?")
            spy_rating = float(spy_rating)

            if spy_rating > 4.5:
                print 'Great ace!'
            elif spy_rating > 3.5 and spy_rating <= 4.5:
                print 'You are one of the good ones.'
            elif spy_rating >= 2.5 and spy_rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'
        else:
            print "you are not eligible to be a spy..please try again .."

    else:
        print "please enter a Valid salutation .. and try again "
else:
    print "please enter a valid username .....and try again"