#functions
def print_two(*args):

    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

print_two("Zed", "Shaw")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
def print_and_return(arg1):
    print(f"And now return {arg1}\n")
    return 500
   



print_two(10, 20)
print_two_again(100,200)
a = print_and_return(100)
print(a)
