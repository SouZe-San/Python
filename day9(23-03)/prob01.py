
def zeroDivision(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(e)
        print("we Couldn't divide by zero")
        
        
def checkRange():
    try:
        x = int(input("Enter a number between 0 to 100: "))
        if(x>100):
            raise ValueError(x)
    except ValueError:
        print("You have Enter a number that put of range")
        
f= open('NOTES.txt')
try:
    print(f.read())
except StopIteration:
    print("some occurs")
    

f.close()


