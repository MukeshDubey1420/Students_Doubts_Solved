import  re

# validation for name
name=raw_input('Enter your name ')
reg='^[a-zA-Z\s]+$'
if not re.match(reg,name):
    print '.invalid name '
else:
    print ' welcome ' , name

#validation for age
age= raw_input('enter you age ')
reg='^[1-9]+[0-9]+$'
if (re.match(reg,age)==None):
    print ' invalid age '
else:
    print 'your age is ', age

#validation for rating
rating=raw_input('enter your rating')
reg='^[1-5]+\.[0-9]'   # make it happen for just integer value ### also for just one place after the decimal
if (re.match(reg,rating)==None):
    print 'invalid rating'
else :
    print ' rating is ', rating

# validation for email
email=raw_input('enter your mail')
reg='^[a-zA-Z0-9]+\@+[a-z]+\.com'
if (re.match(reg,rating)==None):
    print ' invalid email'
else :
    print ' email is ', email
