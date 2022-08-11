#possible actions with file
#close    - close file, like save in editor
#open     - open file  
#read     - read contents of file, can be placed to variable
#write    - write stuff to the file
#readline - reads just one line of text
#truncate - empties the file, be careful if you care about the content
#seek     - move the read/write position to provided position
 

#reading files
from sys import argv        #input varibales from argv, when calling the program
script, filename = argv

#open file
txt = open(filename)
print(f"Your file is {filename}:")
#read the file content and print it
print(txt.read())
txt.close()

#enter file name again by typing it
print("Type the filename again:")
file_again = input("> ")

#open typed file and read its content
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()

#truncate file
txt2 = open(filename, 'w')
print("If you want to exit press Ctrl + C")

print("Truncating the file. Goodbye!")
txt2.truncate()

#write something to the file 
print("Input something to write to file!")
line1 = input('>')
line2 = input('>')
line3 = input('>')

txt2.write(line1)
txt2.write("\n")

txt2.write(line2)
txt2.write("\n")

txt2.write(line3)
txt2.write("\n")

#close file txt2
txt2.close()

#open it again to read, what was written
txt2 = open(filename)

print(txt2.read()) 
#close file
txt2.close()













