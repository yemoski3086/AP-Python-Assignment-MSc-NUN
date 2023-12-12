Graduation_list = ["Musa", "Yasmine", "Aminu"]
for x in Graduation_list:
    print("Dear " + x +"," " I would like to invite you to my Graduation cermony")
Graduation_list[1] = "Adda"
print(Graduation_list)
for x in Graduation_list:
    print("Dear " + x +"," " I would like to invite you to my Graduation cermony")
    print("yasmine cant make it")
#more guests for invitation
    print("i have been allowed more geusts")
Graduation_list.insert(0, "fatima")
Graduation_list.insert(2, "Amina")
Graduation_list.append("Khadija")
print(Graduation_list)
for x in Graduation_list:
    print("Dear " + x +"," " I would like to invite you to my Graduation cermony")
print("i can only invite two guests due to organisational issues")
newlist= Graduation_list.pop(0)
print("Sorry i didnt invite you to my graduation", newlist)
newlist_1= Graduation_list.pop(1)
print("Sorry i didnt invite you to my graduation", newlist_1)
newlist_2=Graduation_list.pop(2)
print("Sorry i didnt invite you to my graduation", newlist_2)
newlist_3=Graduation_list.pop(2)
print("Sorry i didnt invite you to my graduation", newlist_3)
print(Graduation_list)
for x in Graduation_list:
    print("hello " + x +"," " you are still invited to my graduation")
Graduation_list.sort()
print(Graduation_list)
Graduation_list.sort(reverse=True)
print(Graduation_list)
del Graduation_list[0]
print(Graduation_list)
del Graduation_list[0]
print (Graduation_list)
