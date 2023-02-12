str3 = input("Enter A String : ")
wordStock = str3.split(' ')
wordStock = wordStock[::-1]
for i in wordStock:
    print(i, end=" ")