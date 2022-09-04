#own programming

#import exit function from module system(sys)
from sys import exit

#define function to check the value from the list
def check_the_loop():
    loop = ['one', 'two', 'three']

    for i in loop:
        print("In the loop")
         if i == 'two':
           print("i is two, breaking")
           break
        else:
            print("two was not found at this time")


check_the_loop()


def print_smth(rows, lines, what):
    for smth in range(0,rows):
        for smth2 in range(0, lines):
            print(what, end = '')
        print("\n")

print_smth(10, 10, '*')
print_smth(15, 10, '-')








