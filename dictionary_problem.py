dict = {
    "MUKESH DUBEY":29,
    "SANT":18,
    "ISHAN":56,
    "ROHIT":27
    }
print "welcome to the dictionary"
key=raw_input("ENTER KEY TO FIND VALUE :")
if key in dict :
    print "VALUE IS :",dict[key]
else:
     print "not found"