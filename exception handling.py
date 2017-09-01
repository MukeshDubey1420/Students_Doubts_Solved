try :

    a = int(raw_input('enter '))
    assert (a.isalpha()==True), 'Cannot divide alphabets'
    b = int(raw_input('enter'))
    print 'a/b=', a/b
except TypeError:
    print ' wrong input'
except ZeroDivisionError:
    print ' cannot divide by zero'
except ValueError:
    print ' Inavlid input'


