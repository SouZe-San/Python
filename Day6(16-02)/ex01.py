name ={
    "08":"tamal",
    "09": "Biswajit ",
    "24":"Me",
    "16": "Sudip Pedo",
    "28": "subham",
    "26":"Anu Nayak",
    "25":"Bati",
    "python": "pyClass",
    "java": "javaPractice"
}


# !Method 1
# Key_arr = list(name.keys())
# Key_arr.sort()
# for i in Key_arr:
#     print(name[i])

# * Sorted by Keys: ---------->
# !Method 2
key_Sorted = dict(sorted(name.items()))
print(key_Sorted)

# * Sorted By Values :-------------?
values_sorted= dict(sorted(name.items(),key= lambda it : it[1]))

Key = input("Enter The Key: ")
print(name.get(Key))
# print(key_Arr)


title ={
    "hello": "World",
    "classs": "B.tech"
}

name.update(title)
# print(name)
title ={
    "hello": "World",
    "class": "B.tech"
}

name.update(title)
print(name)