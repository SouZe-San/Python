str1 = input("Enter a string: ")
print(str1.capitalize()) # Print The sentence With first latter capitalized ==> Association function
# print(len(str1)) # Print The length of the string ==> Argument function
# str2 = "She will be top on me"  # String is iterable but not immutable
# str2 = str2.replace("She", "I")
# str2 = str2.replace("me", "her")
# print(str2)
# print(str2.count('o', 10, 17))
# print(str2.count('o', 17))  # ==> 10 will take as lower bound
# # print(str2.count('o',10,17))


# passage = " Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deserunt debitis amet quo voluptatibus ducimus qui, est aliquam soluta, vel aliquid ratione quos vero vitae, tempore mollitia nemo beatae sequi Lorem ipsum dolor sit amet consectetur adipisicing elit. Recusandae, commodi facere!orem34 Lorem ipsum dolor sit amet consectetur, adipisicing elit. Obcaecati, necessitatibus sequi tempora iure dolore impedit incidunt vel recusandae. Ut incidunt eos aperiam vitae voluptas nam, unde dolorem perferendis sapiente rerum velit dolorum totam eum voluptatem veritatis, explicabo quam aliquid porro ratione nemo adipisci."

# vowels = ['a', 'e', 'i', 'o', 'u']
# # Method 1
# count = 0
# for vowel in vowels:
#     vowelCount = 0
#     count += passage.lower().count(vowel)
#     vowelCount += passage.lower().count(vowel)
#     print(f"{vowel} is present: {vowelCount}")
# print(count)
# # method 2
# count = 0
# for i in passage:
#     i = i.lower()
#     if i in vowels:
#         count += 1
# print(count)

# str3 = "Hello My friend"
# # lower = input("enter the Lower Case: ")
# # upper = input("enter the upper Case: ")
# # str3 = str3.replace(lower, upper)
# # print(str3)

# str4 = "   welcome to Heaven   "
# print(str4.lstrip())  # --. Remove spaces from the first side of the string
# print(str4.rstrip())  # --. Remove spaces from the End side of the string
# print(str4.strip())  # --. Remove spaces from the Both side of the string

# print(str3[-1:: -1])

# wordStock = []
# wordStock = str3.split(' ')
# print(wordStock[::-1])  # --> Reverse the list of words
# print(str3)

# for i in wordStock:
#     print(i[::-1], end=" ")

# print(chr(97))
print(int("A"))
