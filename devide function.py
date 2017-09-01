def divide(a,b):
    print ' division gives' , a/b

def swap(a,b):
    print 'a=',a
    print 'b =', b
    temp=a
    a=b
    b=temp
    print ' a=' , a
    print ' b=', b

a=int(raw_input('enter first'))
b=int(raw_input('enter second'))
divide(a,b)
swap(a,b)
divide(a,b)


