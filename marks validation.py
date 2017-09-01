
grade='A'
name='Mukesh'

#if __name__=='main':
print ' marks.py is running'
marks=raw_input('enter marks')
if float(marks)>9:
        print ' A'
        grade='A'
elif float(marks)>8:
        print'B'
        grade='B'
elif float(marks)>7:
        print'C'
        grade='C'
else :
        print ' you have no result'
        grade='F'

print ' out of if statement'
