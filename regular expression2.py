from re import match , search , sub


str='My name is Python ..... Hello everyone '
if match('name', str):
    print ' found using match function'
else :
    print ' not found'

if search('name', str):
    print ' found using search  function'
else :
    print ' not found'

str="my name is sant"
st=sub(' ','-',str)
str= sub('sant','python',str)

print str
print st