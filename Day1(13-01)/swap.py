
# ! PROGRAM : 1: Swapping of 2 varbers without using 3rd variable
a = 10
b = 20
# * Swapping the Numbers Without 3rd variable .. Static input 
a = a + b
b = a-b
a = a-b
print("The First number is: " ,a)
print("The second number is: " ,b)


# * Swapping the Numbers Without 3rd variable .. Dynamic input 
var1 = input(" Enter The first input: ")
var2 = input(" Enter The second input: ")
var1 = var1, var2
var2 = var1[0]
var1 = var1[1]
print("The First input is: " ,var1)
print("The second input is: ",var2)
# * printing