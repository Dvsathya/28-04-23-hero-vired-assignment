s = input("Enter string : ")
str1 = s.lower()
list1 = []
for i in str1:
    if i not in list1:
        list1.append(i)
for x in range(len(list1)):
    if x != len(list1) - 1:
        print(list1[x],end = ",")
    else:
        print(list1[x])
#printing of unique letters
