
# capitalise the string
# -count no of vowels
# -use uppercase
# -use lowercase
# -count of no of elements in string
# - count no of vowels


str = input("Enter A String : ")

# String Operation
print("After Capitalized:: ", str.capitalize())
print("Transform to LowerCase :: ", str.lower())
print("Transform to UpperCase :: ", str.upper())
print("How Many Letter present in string:-> ", len(str))


vowels = ['a', 'e', 'i', 'o', 'u']
# Count Number of Vowel
count = 0
for vowel in vowels:
    vowelCount = 0
    count += str.lower().count(vowel)
    vowelCount += str.lower().count(vowel)
    print(f"{vowel} is present: {vowelCount}")
print("The Total vowel In String is: ",count)
