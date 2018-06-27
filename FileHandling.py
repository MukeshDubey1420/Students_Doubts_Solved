# file = open("Sample.txt" , "r")
# print( file.read())    #The output of that command will display all the text inside the file.
# print(file.read(5))    #following code the interpreter will read the first five characters of stored data and return it as a string:

# print(file.readline())
# print(file.readline())   #Each time you run the method, it will return a string of characters that contains a single line of information from the file.
# print(file.readline())


# print(file.readlines()) #readlines() returns a list of strings in which each element is a string of the line.


# for line in file:       #use the loop over method. The advantage to using this method is that the related code is both simple and easy to read.
#     print(line)
file = open("Sample.txt" , "w")
file.write("This is a test")
file.write("To add more lines.")        #This will append two line at the end, into the file that we have considered.
lines_of_text = ["One line of text here", "and another line here", "and yet another here"]  # also use this to write multiple lines to a file at once:
file.writelines(lines_of_text)
file.close()
file = open("Sample.txt" , "r")
print(file.read())
file.close()
